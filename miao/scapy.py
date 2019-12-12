import scrapy
class Ngaspider(scrapy.Spider):
    name='NgaSpider'
    host='http://www.baidu.com'
    start_urls=['http://jingyan.baidu.com/article/14bd256e748346bb6d2612be.html']
    def parse(self, response):
        print(response.body)

Ngaspider()