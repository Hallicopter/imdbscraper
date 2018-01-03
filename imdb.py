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
            runtime = film.xpath("p[1]/span/text()").extract()
            runtime = re.findall(r'[0-9]+', str(runtime))
            director = film.xpath("p/text()").extract()
            actor = film.xpath("p/text()").extract()

            if "Director" in str(director):
                director = film.xpath("p[3]/a/text()").extract()[0]
            else:
                director = "N/A"
            if "Stars" in str(actor):
                actor = film.xpath("p[3]/a/text()").extract()[1:]
            else:
                actor = "N/A"
            if runtime == []:
                runtime = "N/A"
            else:
                print('This', runtime)
                runtime = runtime[0]

            film_dat = {
                'release': re.findall(r'\(([^)]+)\)',str(film.xpath("h3/span/text()").extract()))[0],
                'runtime': runtime,
                'film_name' :film.xpath("h3[1]/a[1]/text()").extract(),
                'director'  : director,
                'lead_actors': actor,
                'imdb_link' : 'http://www.imdb.com'+film.xpath("h3[1]/a[1]/@href").extract()[0]
            }
            yield film_dat
        # Follow the pagination link
        next_page_url = response.xpath("//div[1]/div[1]/div[4]/div[1]/a/@href").extract()
        for url in next_page_url:
            if 'adv_nxt' in url:
                url = response.urljoin(url)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',url)
                yield scrapy.Request(url=url, callback=self.parse)
                break
