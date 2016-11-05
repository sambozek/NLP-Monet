from monet_spider.items import MonetInformation


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose


class MonetSpider(BaseSpider):
    """Spider to grab all information of Monet's Works on theartstory.org"""
    name = 'theartstory'
    allowed_domains = ['theartstory.org']
    start_urls = ['http://www.theartstory.org/artist-monet-claude-artworks.htm']

    description_xpath = "//tr[@class='artwork-row']/td"

    artwork_fields = {
    'title_year': "//td[@class='desc-col']/h4[@class='artwork-title']",
    'Description': "//td[@class='desc-col']/p[@class='artwork-desc']"
    }
    def parse(self, response):
        """"Call back used by Scrapy to download and process response
        """
        selector = HtmlXPathSelector(response)

        # Go through art statements
        for statement in selector.select(self.description_xpath):
            loader = XPathItemLoader(MonetInformation(), selelctor=statement)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor
