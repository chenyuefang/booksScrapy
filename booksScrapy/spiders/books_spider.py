from scrapy.spiders import Spider  # 爬虫模式
from scrapy import Request  # 请求模式
import re
from booksScrapy.items import BooksScrapyItem  # 导入Item类


class booksSpider(Spider):
    name = "books"  # 爬虫的名字
    start_urls = ["http://books.toscrape.com/"]

    # 爬虫功能
    def parse(self, response):
        # 数据提取功能
        li_selector = response.xpath("//ol/li")

        for li in li_selector:
            #  导入item
            item = BooksScrapyItem()  # 生成了Item类的对象
            name = li.xpath("article/h3/a/text()").extract_first()  # .extract_first() 等同于 .extract()[0]  提取第一个
            price = li.xpath("article/div[last()]/p[@class='price_color']/text()").extract()[0]
            print(name)
            item["name"] = name  # 书籍名称
            item["price"] = price  # 书籍价格
            yield item

        next_url = response.xpath("//li[@class='next']/a/@href").extract()
        if next_url:
            next_url = "http://books.toscrape.com/catalogue/page-" + re.sub("\D", "", next_url[0]) + ".html"
            yield Request(next_url, callback=self.parse)
