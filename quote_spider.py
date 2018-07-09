import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/'
    ]

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').extract_first().strip(),
                'author': quote.xpath('span/small/text()').extract_first()
            }

            next_page = response.css('li.next a::attr("href")').extract_first()
            if next_page is not None:
            	yield response.follow(next_page, self.parse)
