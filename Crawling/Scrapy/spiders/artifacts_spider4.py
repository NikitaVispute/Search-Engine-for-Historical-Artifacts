import scrapy

class ArtifactsSpider(scrapy.Spider):
    name = "artifacts4"
    allowed_domains = ['metmuseum.org']
    start_urls = [
        # 'https://www.metmuseum.org/art/collection/search/61656?searchField=All&amp;sortBy=Relevance&amp;deptids=6&amp;ft=*&amp;offset=0&amp;rpp=20&amp;pos=19',
        # 'https://www.metmuseum.org/art/collection/search/551811?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=40&amp;rpp=20&amp;pos=43',
        # 'https://www.metmuseum.org/art/collection/search/555531?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=40&amp;rpp=20&amp;pos=48',
        # 'https://www.metmuseum.org/art/collection/search/544486?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=40&amp;rpp=20&amp;pos=47',
        # 'https://www.metmuseum.org/art/collection/search/544450?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=80&amp;rpp=20&amp;pos=90',
        'https://www.metmuseum.org/art/collection/search/545072?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=2',
        'https://www.metmuseum.org/art/collection/search/544765?searchField=All&amp;sortBy=Relevance&amp;deptids=10&amp;ft=*&amp;offset=80&amp;rpp=80&amp;pos=101',        
        'https://www.metmuseum.org/art/collection/search/252090?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=31',
        'https://www.metmuseum.org/art/collection/search/247417?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=30',
        'https://www.metmuseum.org/art/collection/search/248205?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=54',
        # 'https://www.metmuseum.org/art/collection/search/253638?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=62',
        # 'https://www.metmuseum.org/art/collection/search/242162?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=80&amp;rpp=80&amp;pos=156',
        # 'https://www.metmuseum.org/art/collection/search/242233?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=80&amp;rpp=80&amp;pos=153',
        # 'https://www.metmuseum.org/art/collection/search/243513?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=240&amp;rpp=80&amp;pos=302',
        # 'https://www.metmuseum.org/art/collection/search/256570?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=240&amp;rpp=80&amp;pos=314',
        # 'https://www.metmuseum.org/art/collection/search/248715?searchField=All&amp;sortBy=Relevance&amp;deptids=13&amp;ft=*&amp;offset=240&amp;rpp=80&amp;pos=320',
        # 'https://www.metmuseum.org/art/collection/search/451073?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=4',
        # 'https://www.metmuseum.org/art/collection/search/444596?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=9',
        # 'https://www.metmuseum.org/art/collection/search/451379?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=16',
        # 'https://www.metmuseum.org/art/collection/search/443060?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=27',
        # 'https://www.metmuseum.org/art/collection/search/446808?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=35',
        # 'https://www.metmuseum.org/art/collection/search/706073?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=51',
        # 'https://www.metmuseum.org/art/collection/search/447017?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=50',
        # 'https://www.metmuseum.org/art/collection/search/455426?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=0&amp;rpp=80&amp;pos=79',
        # 'https://www.metmuseum.org/art/collection/search/452553?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=320&amp;rpp=80&amp;pos=380',
        # 'https://www.metmuseum.org/art/collection/search/444473?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=320&amp;rpp=80&amp;pos=378',
        # 'https://www.metmuseum.org/art/collection/search/445017?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=480&amp;rpp=80&amp;pos=503',
        # 'https://www.metmuseum.org/art/collection/search/81703?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=480&amp;rpp=80&amp;pos=515',
        # 'https://www.metmuseum.org/art/collection/search/446942?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=480&amp;rpp=80&amp;pos=527',
        # 'https://www.metmuseum.org/art/collection/search/451386?searchField=All&amp;sortBy=Relevance&amp;deptids=14&amp;ft=*&amp;offset=480&amp;rpp=80&amp;pos=554',
        # 'https://www.metmuseum.org/art/collection/search/78195?&pkgids=538&ft=*&pg=2&rpp=20&amp;pos=39',
        # 'https://www.metmuseum.org/art/collection/search/37789?&pkgids=538&ft=*&pg=2&rpp=20&amp;pos=33',
        # 'https://www.metmuseum.org/art/collection/search/38021?&pkgids=538&ft=*&offset=0&rpp=20&amp;pos=15',
        # 'https://www.metmuseum.org/art/collection/search/37558?&pkgids=537&ft=*&pg=2&rpp=20&amp;pos=32',
        # 'https://www.metmuseum.org/art/collection/search/37557?&pkgids=537&ft=*&pg=2&rpp=20&amp;pos=30',
        # 'https://www.metmuseum.org/art/collection/search/63532?&pkgids=537&ft=*&offset=0&rpp=20&amp;pos=11',
        # 'https://www.metmuseum.org/art/collection/search/39111?&pkgids=537&ft=*&offset=0&rpp=20&amp;pos=9',
        # 'https://www.metmuseum.org/art/collection/search/38039?&pkgids=536&ft=*&pg=3&rpp=20&amp;pos=56',
        # 'https://www.metmuseum.org/art/collection/search/61429?&pkgids=536&ft=*&pg=3&rpp=20&amp;pos=57',
        # 'https://www.metmuseum.org/art/collection/search/65584?&pkgids=536&ft=*&pg=3&rpp=20&amp;pos=52',
        # 'https://www.metmuseum.org/art/collection/search/75909?&pkgids=536&ft=*&pg=3&rpp=20&amp;pos=47',
        # 'https://www.metmuseum.org/art/collection/search/74425?&pkgids=536&ft=*&pg=3&rpp=20&amp;pos=44',
        # 'https://www.metmuseum.org/art/collection/search/37397?&pkgids=536&ft=*&pg=2&rpp=20&amp;pos=37',
        # 'https://www.metmuseum.org/art/collection/search/39328?&pkgids=536&ft=*&pg=2&rpp=20&amp;pos=33',
        # 'https://www.metmuseum.org/art/collection/search/38127?&pkgids=536&ft=*&pg=2&rpp=20&amp;pos=28',
        # 'https://www.metmuseum.org/art/collection/search/38583?&pkgids=536&ft=*&pg=2&rpp=20&amp;pos=24',
        # 'https://www.metmuseum.org/art/collection/search/38435?&pkgids=536&ft=*&pg=2&rpp=20&amp;pos=21',
        # 'https://www.metmuseum.org/art/collection/search/38104?&pkgids=536&ft=*&offset=0&rpp=20&amp;pos=15',
        # 'https://www.metmuseum.org/art/collection/search/38237?&pkgids=536&ft=*&offset=0&rpp=20&amp;pos=6',
        # 'https://www.metmuseum.org/art/collection/search/51279?&pkgids=536&ft=*&offset=0&rpp=20&amp;pos=3',
        # 'https://www.metmuseum.org/art/collection/search/76114?&pkgids=535&ft=*&pg=2&rpp=20&amp;pos=26',
        # 'https://www.metmuseum.org/art/collection/search/40524?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=17',
        # 'https://www.metmuseum.org/art/collection/search/42308?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=13',
        # 'https://www.metmuseum.org/art/collection/search/39957?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=14',
        # 'https://www.metmuseum.org/art/collection/search/50444?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=11',
        # 'https://www.metmuseum.org/art/collection/search/39881?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=9',
        # 'https://www.metmuseum.org/art/collection/search/50356?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=4',
        # 'https://www.metmuseum.org/art/collection/search/50325?&pkgids=535&ft=*&offset=0&rpp=20&amp;pos=3',
        # 'https://www.metmuseum.org/art/collection/search/50342?&pkgids=534&ft=*&offset=0&rpp=20&amp;pos=5',
        # 'https://www.metmuseum.org/art/collection/search/50342?&pkgids=534&ft=*&offset=0&rpp=20&amp;pos=5',
        # 'https://www.metmuseum.org/art/collection/search/39707?&pkgids=534&ft=*&offset=0&rpp=20&amp;pos=4',
        # 'https://www.metmuseum.org/art/collection/search/44859?&pkgids=534&ft=*&offset=0&rpp=20&amp;pos=6',
        # 'https://www.metmuseum.org/art/collection/search/60870?&pkgids=533&ft=*&pg=2&rpp=20&amp;pos=22',
        # 'https://www.metmuseum.org/art/collection/search/39637?&pkgids=533&ft=*&offset=0&rpp=20&amp;pos=17',
        # 'https://www.metmuseum.org/art/collection/search/49156?&pkgids=533&ft=*&offset=0&rpp=20&amp;pos=13',
        # 'https://www.metmuseum.org/art/collection/search/42183?&pkgids=533&ft=*&offset=0&rpp=20&amp;pos=11',
        # 'https://www.metmuseum.org/art/collection/search/42162?&pkgids=533&ft=*&offset=0&rpp=20&amp;pos=6'
    ]
    
    def parse(self, response):

        for title in response.css('span.artwork__title--text'):
            title = title.css('span::text').extract()

        for art in response.css('div.artwork__intro__desc'):
                info = art.css('p::text').extract()
           
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
            
           anchors = response.css('h4.card__title a')
           yield from response.follow_all(anchors, callback=self.parse)
           # NEXT_PAGE_SELECTOR = '.card__title + a::attr(href)'
           # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
           # if next_page:
           #     yield scrapy.Request(
           #     response.urljoin(next_page),
           #     callback=self.parse)

