# -*- coding: utf-8 -*-
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/search/title?countries=in&languages=hi&title_type=feature']

    def parse(self, response):
        self.log('Just visited '+ response.url)
        films_src = response.xpath("//div[1]/div[1]/div[3]/div/div[3]").extract_first()
        
        for film in films_src:
            film{
                'film_name':films_src.xpath("h3[1]/a[1]/text()").extract(),
                'director': films_src.xpath("p[3]/a/text()").extract()[0],
                'lead_actors': films_src.xpath("p[3]/a/text()").extract()[1:],
                'imdb_link': 'http://www.imdb.com'+films_src.xpath("h3[1]/a[1]/@href").extract()[0]
            }
