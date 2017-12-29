# -*- coding: utf-8 -*-
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    src = 'http://www.imdb.com/search/title?countries=%C2%B7%C2%B7%C2%B7%C2%A0Common%20Countries%C2%A0%C2%B7%C2%B7%C2%B7&groups=top_100&languages=%C2%B7%C2%B7%C2%B7%C2%A0Common%20Languages%C2%A0%C2%B7%C2%B7%C2%B7&title_type=feature'
    start_urls = [src]

    def parse(self, response):
        self.log('Just visited '+ response.url)
        films_src = response.xpath("//div[1]/div[1]/div[3]/div/div[3]")
        for film in films_src:
            film_dat = {
                'film_name' :film.xpath("h3[1]/a[1]/text()").extract(),
                'director'  : film.xpath("p[3]/a/text()").extract()[0],
                'lead_actors': film.xpath("p[3]/a/text()").extract()[1:],
                'imdb_link' : 'http://www.imdb.com'+film.xpath("h3[1]/a[1]/@href").extract()[0]
            }
            yield film_dat
        # Follow the pagination link
        next_page_url = response.xpath("//div[1]/div[1]/div[4]/div[1]/a[1]/@href").extract()[0]
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
