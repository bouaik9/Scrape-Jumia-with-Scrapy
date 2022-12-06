import scrapy


class JumiaSpiderSpider(scrapy.Spider):
    name = 'jumia_spider'
    allowed_domains = ['jumia.ma']
    start_urls = ['https://www.jumia.ma/vetements-hommes/'] #paste link that contains products to scrap

    def parse(self, response):
        products = response.css("div.info") #list of products
        for product in products:
            yield {
                'name': product.css('h3.name::text').get(),  #product name
                'price': product.css('div.prc::text').get()  #prodcut price
            }
        #get the link of the second , third ...page
        next_url = response.css('a.pg::attr(href)').get()
        if next_url is not None:
            next_page = 'jumia.ma' + next_url
            yield scrapy.Request(next_page, callback=self.parse)
