from scrapy import Spider, Request
from loreal.items import LorealItem

class LorealSpider(Spider):
	name = 'loreal_spider'

	start_urls = 'https://www.lorealparisusa.com/products/hair-care/shop-all-products.aspx?size=21&page=1'

	allowed_urls = 'https://www.lorealparisusa.com/'


	def parse(self, repsonse):
		num_pages_



