from monet_spider.items import MonetInformation
from scrapy.spider import BaseSpider


class MonetSpider(BaseSpider):
    """Spider to grab all information of Monet's Works on theartstory.org"""
    name = 'theartstory'
    allowed_domains = ['theartstory.org']
    start_urls = ['http://www.theartstory.org/artist-monet-claude-artworks.htm']

    description_xpath = "//tr[@class='artwork-row']/td"

    artwork_fields = {
    'title_year': "//td[@class='desc-col']/h4[@class='artwork-title']"
    }
