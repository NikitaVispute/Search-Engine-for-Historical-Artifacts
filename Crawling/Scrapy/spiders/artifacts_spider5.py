import scrapy

class ArtifactsSpider(scrapy.Spider):
    name = "artifacts5"
    allowed_domains = ['louvre.fr']
    start_urls = [
        'https://www.louvre.fr/en/oeuvre-notices/frog-oil-lamp'
    ]
    
    def parse(self, response):

        for title in response.css('h1.title-13'):
            title = title.css('span::text').extract()

        for art in response.css('div.col-desc'):
                info = art.css('p strong::text').extract()
           
        row_data=zip(title,info)

        #Making extracted data row wise
        for item in row_data:
           #create a dictionary to store the scraped info
           scraped_info = {
                #key:value
                'page': response.url,
                'title' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'info' : item[1]
           }

           #yield or give the scraped info to scrapy
           yield scraped_info
           
           next_page = response.css('div.col-3 a::attr(href)').get()
           if next_page is not None:
            yield response.follow(next_page, self.parse) 
           # anchors = response.css('h4.card__title a')
           # yield from response.follow_all(anchors, callback=self.parse)
           # NEXT_PAGE_SELECTOR = '.card__title + a::attr(href)'
           # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
           # if next_page:
           #     yield scrapy.Request(
           #     response.urljoin(next_page),
           #     callback=self.parse)

