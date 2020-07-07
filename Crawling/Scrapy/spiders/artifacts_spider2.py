import scrapy


class ArtifactsSpider(scrapy.Spider):
    name = "artifacts2"
    allowed_domains = ['joyofmuseums.com']
    start_urls = [
        'https://joyofmuseums.com/museums/europe/germany-museums/berlin-museums/altes-museum/',
        'https://joyofmuseums.com/museums/africa-museums/egypt-museums/cairo-museums/egyptian-museum/',
        'https://joyofmuseums.com/museums/europe/germany-museums/berlin-museums/the-pergamon-museum/',
        'https://joyofmuseums.com/museums/europe/germany-museums/berlin-museums/neues-museum/',
    ]
    
    def parse(self, response):

        print("processing:"+response.url)
        #Extract data using css selectors
        page=response.css('.post-content  h2 ul li a::attr(href)').extract() 
        title=response.css('.post-content h2 ul li a::text').extract()
        info=response.css('.post-content h2 ul li ul li::text').getall()
       
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
