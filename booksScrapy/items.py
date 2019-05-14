# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    # 修改定义
    name = scrapy.Field() # 书籍名称
    price = scrapy.Field() # 书籍价格
    url = scrapy.Field # 链接地址
