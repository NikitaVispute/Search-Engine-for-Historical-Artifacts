import scrapy

class ArtifactsSpider(scrapy.Spider):
    name = "artifacts3"
    allowed_domains = ['getty.edu']
    start_urls = [
        'http://www.getty.edu/art/collection/objects/6554/unknown-maker-statue-of-a-kore-the-elgin-kore-greek-about-475-bc/',
        'http://www.getty.edu/art/collection/objects/6549/unknown-maker-statue-of-hercules-lansdowne-herakles-roman-about-ad-125/',
        'http://www.getty.edu/art/collection/objects/7596/attributed-to-kleophrades-painter-attic-panathenaic-amphora-greek-attic-500-480-bc/?dz=#f53c2ec7df9828ba887f19cf54ef8bbfaf857954',
        'http://www.getty.edu/art/collection/objects/9421/attributed-to-the-isidora-master-mummy-portrait-of-a-woman-romano-egyptian-ad-100/',
        'http://www.getty.edu/art/collection/objects/7303/unknown-maker-sculptural-group-of-a-seated-poet-and-sirens-2-with-unjoined-fragmentary-curls-304-greek-tarantine-350-300-bc/',
        'http://www.getty.edu/art/collection/objects/7041/unknown-maker-statue-of-jupiter-marbury-hall-zeus-roman-100-1-bc/',
        'http://www.getty.edu/art/collection/objects/10890/unknown-maker-cameo-glass-skyphos-roman-25-bc-ad-25/',
        'http://www.getty.edu/art/collection/objects/29682/workshop-of-the-calabresi-urn-white-on-red-ware-pithos-with-lid-etruscan-650-625-bc/?dz=#a9ff034f040a1d7194295506f00e45d3b647129c',
        'http://www.getty.edu/art/collection/objects/10949/unknown-maker-male-harp-player-of-the-early-spedos-type-cycladic-2700-2300-bc/',
        'http://www.getty.edu/art/collection/objects/7792/unknown-maker-statue-of-a-victorious-youth-greek-300-100-bc/?dz=#68788f24efae95841e79b70adf1a8cc848572090',
        'http://www.getty.edu/art/collection/objects/284651/gian-lorenzo-bernini-bust-of-pope-paul-v-italian-1621/?dz=#6dc75e5141ccf8566b8a3dc455fc424edd733c58',
        'http://www.getty.edu/art/collection/objects/266018/auguste-rodin-christ-and-mary-magdalene-french-1908/',
        'http://www.getty.edu/art/collection/objects/295865/unknown-maker-the-borghese-windsor-cabinet-italian-cabinet-french-stand-cabinet-about-1620-stand-before-1821/',
        'http://www.getty.edu/art/collection/objects/936/giambologna-giovanni-da-bologna-or-jean-de-boulogne-female-figure-possibly-venus-formerly-titled-bathsheba-flemish-1571-1573/',
        'http://www.getty.edu/art/collection/objects/1207/adriaen-de-vries-juggling-man-dutch-about-1615/',
        'http://www.getty.edu/art/collection/objects/220395/jean-antoine-houdon-bust-of-marie-sebastien-charles-francois-fontaine-de-bire-french-1785/',
        'http://www.getty.edu/art/collection/objects/198578/meissen-porcelain-manufactory-model-by-johann-joachim-kandler-a-turkey-german-about-1733/',
        'http://www.getty.edu/art/collection/objects/5607/attributed-to-andre-charles-boulle-and-medallions-after-jean-varin-cabinet-on-stand-french-about-1675-1680/?dz=#944876cae6649534f796b0762c583ff402ced543',
        "http://www.getty.edu/art/collection/objects/226276/francois-thomas-germain-la-machine-d'argent-or-centerpiece-for-a-table-surtout-de-table-french-1754/'", 
        "http://www.getty.edu/art/collection/objects/5806/beauvais-manufactory-woven-under-the-direction-of-philippe-behagle-after-cartoons-by-guy-louis-vernansal-et-al-tapestry-les-astronomes-from-l'histoire-de-l'empereur-de-la-chine-series-french-about-1697-1705/'",       
        'http://www.getty.edu/art/collection/objects/1138/fontana-workshop-possibly-orazio-fontana-or-possibly-flaminio-fontana-basin-with-deucalion-and-pyrrha-italian-about-1565-1575/',
        'http://www.getty.edu/art/collection/objects/5470/attributed-to-david-roentgen-gilt-bronze-plaque-attributed-to-pierre-gouthiere-mounts-by-francois-remond-rolltop-desk-german-1787-1788/',
        'http://www.getty.edu/art/collection/objects/336767/dioskourides-intaglio-with-bust-of-demosthenes-roman-about-25-bc/',
        'http://www.getty.edu/art/collection/objects/336737/unknown-maker-engraved-scaraboid-with-perseus-greek-400-350-bc/',
        'http://www.getty.edu/art/collection/objects/327217/unknown-maker-applique-depicting-the-sun-god-usil-etruscan-500-475-bc/?dz=#3346028db30a5bd09b86640bd59a611f70fa30fb',
        "http://www.getty.edu/art/collection/objects/333351/unknown-maker-funerary-relief-of-hadirat-katthina-daughter-of-sha'ad-palmyran-ad-200-220/",
        'http://www.getty.edu/art/collection/objects/336764/unknown-maker-intaglio-with-bust-of-antinous-roman-ad-131-138/',
        'http://www.getty.edu/art/collection/objects/327105/unknown-maker-relief-with-theater-masks-roman-1st-century-ad/?dz=#3d4d51fc97e800e5b40eba85daf6a290dfb8cf01',
        'http://www.getty.edu/art/collection/objects/326000/unknown-maker-geometric-amphora-greek-775-750-bc/',
        'http://www.getty.edu/art/collection/objects/325999/attributed-to-the-timiades-painter-neck-amphora-with-a-erotic-scene-and-b-man-and-woman-between-sphinxes-greek-attic-565-550-bc/',
        'http://www.getty.edu/art/collection/objects/340870/giovanni-di-balduccio-the-annunciation-italian-about-1333-1334/',
        'http://www.getty.edu/art/collection/objects/337384/veit-stoss-corpus-christi-german-about-1490-1500/',
        'http://www.getty.edu/art/collection/objects/328670/auguste-rodin-bust-of-john-the-baptist-french-model-1880-cast-1886/?dz=#d92e3d69dcecc2e14fe3a7f36fcc5ce3aa0ba8c1',
        'http://www.getty.edu/art/collection/objects/326677/desiderio-da-settignano-bust-of-a-young-boy-italian-about-1460-1464/?dz=#a1897d773b6c594712b391c5505ef6ea12c2cd82',
        'http://www.getty.edu/art/collection/objects/294078/wouter-crabeth-the-prophet-habakkuk-and-the-angel-netherlandish-about-1565/',
        'http://www.getty.edu/art/collection/objects/337412/juan-conchillos-falco-saint-john-the-baptist-spanish-november-9-1695/',
        'http://www.getty.edu/art/collection/objects/328113/edme-bouchardon-hercules-subduing-the-centaurs-french-about-1735-1740/',
        "http://www.getty.edu/art/collection/objects/5806/beauvais-manufactory-woven-under-the-direction-of-philippe-behagle-after-cartoons-by-guy-louis-vernansal-et-al-tapestry-les-astronomes-from-l'histoire-de-l'empereur-de-la-chine-series-french-about-1697-1705/",
        'http://www.getty.edu/art/collection/objects/226430/peter-paul-rubens-the-calydonian-boar-hunt-flemish-about-1611-1612/',
        'http://www.getty.edu/art/collection/objects/333122/eustache-le-sueur-crucifixion-french-about-1650-1655/'
    ]
    
    def parse(self, response):

        for title in response.css('#utilities-row'):
            title = title.css('h2::text').extract()
        
        for art in response.css('#detail-text'):
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
            
            # NEXT_PAGE_SELECTOR = '.maxbutton-1.maxbutton.maxbutton-popular-paintings + a::attr(href)'
            # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # if next_page:
            #     yield scrapy.Request(
            #     response.urljoin(next_page),
            #     callback=self.parse)

