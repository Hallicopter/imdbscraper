# -*- coding: utf-8 -*-
import scrapy
import re

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    

    def __init__(self, search = None, *args, **kwargs):
        self.start_urls = [search ]
        super().__init__(**kwargs)
        
    def parse(self, response):
        self.log('Just visited '+ response.url)
        films_src = response.xpath("//div[1]/div[1]/div[3]/div/div[3]")
        for film in films_src:
            runtime = film.xpath("p[1]/span[3]/text()").extract()[0]
            if runtime == None:
                runtime = "N/A"
            else:
                runtime = re.findall(r'[0-9]+', runtime)[0]

            film_dat = {
                'runtime': runtime,
                'film_name' :film.xpath("h3[1]/a[1]/text()").extract(),
                'director'  : film.xpath("p[3]/a/text()").extract()[0],
                'lead_actors': film.xpath("p[3]/a/text()").extract()[1:],
                'imdb_link' : 'http://www.imdb.com'+film.xpath("h3[1]/a[1]/@href").extract()[0]
            }
            yield film_dat
        # Follow the pagination link
        next_page_url = response.xpath("//div[1]/div[1]/div[4]/div[1]/a[1]/@href").extract()[0]
        if 'adv_nxt' in next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
