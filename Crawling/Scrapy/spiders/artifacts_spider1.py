import scrapy

class ArtifactsSpider(scrapy.Spider):
    name = "artifacts1"
    allowed_domains = ['joyofmuseums.com']
    start_urls = [
        'https://joyofmuseums.com/most-popular/most-popular-historical-objects/',
        'https://joyofmuseums.com/most-popular/most-popular-sculpture/',
        'https://joyofmuseums.com/most-popular/egyptian-art/',
        'https://joyofmuseums.com/most-popular/popular-buddhist-art/',
    ]
    
    def parse(self, response):

        print("processing:"+response.url)
        #Extract data using css selectors
        page=response.css('h3 a::attr(href)').extract() 
        title=response.css('h3 a::text').extract()
        info=response.css('p::text').extract()
       
        row_data=zip(page, title, info)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page': item[0],
                'title' : item[1], #item[0] means product in the list and so on, index tells what value to assign
                'info' : item[2],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
            
            # NEXT_PAGE_SELECTOR = '.maxbutton-1.maxbutton.maxbutton-popular-paintings + a::attr(href)'
            # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # if next_page:
            #     yield scrapy.Request(
            #     response.urljoin(next_page),
            #     callback=self.parse)

