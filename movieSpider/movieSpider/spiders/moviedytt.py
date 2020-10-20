import scrapy
import  re
from ..items import MoviespiderItem

class MoviedyttSpider(scrapy.Spider):
    name = 'moviedytt'
    allowed_domains = ['dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/list_23_1.html']

    def parse(self, response):
        #获取电影详情链接
        all_urls = response.xpath("//div[@class='co_content8']/ul//a/@href").getall()
        for url in  all_urls:
            try:
                # detail_url = re.search('/html.+?\.html',url).group()
                new_detail = response.urljoin(url)
                yield scrapy.Request(new_detail,callback=self.parse_detail)
            except Exception as ec:
                print(ec)
                break
        #爬取前两页
        for i in range(2,3):
            url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_%s.html'%i
            yield scrapy.Request(url,callback=self.parse)

    def parse_detail(self,response):
        push_date = response.xpath("//div[@class='co_content8']/ul/text()").get().strip()
        all_list = response.xpath("//div[@class='co_content8']/ul//p/text()").getall()
        detail = "".join(all_list)
        new_detail = "".join(detail.split())
        item = MoviespiderItem(detail = new_detail)
        yield item






