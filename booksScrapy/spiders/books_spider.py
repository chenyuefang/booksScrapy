from scrapy.spiders import Spider  # 爬虫模式
from scrapy import Request  # 请求模式
from booksScrapy.items import BooksscrapyItem  # 导入Item类


class booksSpider(Spider):
    name = 'books'  # 爬虫的名字
    start_urls = ["http://books.toscrape.com/"]

    # 爬虫功能
    def parse(self, response):
        # 数据提取功能
        li_selector = response.expath("//oi/li")
        for li in li_selector:
            #  导入item
            item = BooksscrapyItem()  # 生成了Item 类的对象
        name = li.expath("article/h3/a/text()").extract_first()
        price = li.expath("article/div[last()]/p[@class=/text()").extract()[0]
        item["name"] = name  # 书籍名称
        item["price"] = price  # 书籍价格
        yield item
