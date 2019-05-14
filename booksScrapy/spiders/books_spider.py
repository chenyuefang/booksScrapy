
from scrapy.spiders import Spider  # 爬虫模式
from scrapy import Request  # 请求模式


class booksSpider(Spider):
    name = 'books'  # 爬虫的名字
    start_urls = ["http://books.toscrapr.com/"]

    # 爬虫功能
    def parse(self, response):
        print(response.text)

    # 数据提取功能
    li_selector = response.expath("//oi/ol")

