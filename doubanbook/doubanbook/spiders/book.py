# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["book.douban.com"]
    start_urls = (
        'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91',
    )

    def parse(self, response):
        # for sel in response.xpath('//ul/li[@class="subject-item"]'):
        #     item=DoubanbookItem()
        #     item['author']=sel.xpath('div[@class="info"]/h2/a/text()[1]').extract()
        #     item['score']=sel.xpath('div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
        #     yield item

        next_page_url = response.xpath('//a/@href').extract()

        yield next_page_url