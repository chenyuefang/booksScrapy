# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BooksscrapyPipeline(object):

    def process_item(self, item, spider):
        # 处理数据
        with open("books.txt","a",encoding="utf-8") as f:
            book_str = item["name"] + ":" +item["price"] + "\n"
            f.write(book_str)

         return item
    # 爬虫全部完成后执行一次
    def close_spider(self):
        pass