from scrapy.item import Item, Field

class MonetInformation(Item):
	"""Scrape Monet Painting Interpretation Into Container"""
	title = Field()
    description = Field()

