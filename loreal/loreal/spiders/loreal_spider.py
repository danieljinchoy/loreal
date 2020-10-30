from scrapy import Spider, Request
from loreal.items import LorealItem

class LorealSpider(Spider):
	name = 'loreal_spider'

	start_urls = 'https://www.lorealparisusa.com/products/hair-care/shop-all-products.aspx?size=21&page=1'

	allowed_urls = 'https://www.lorealparisusa.com/'


	def parse(self, repsonse):
		num_pages_haircare = len(response.xpath('//div[@class="results-pagination"]/a').extract()) - 2

		num_pages_skincare = len(response.xpath('//div[@class="results-pagination"]/a').extract()) - 2

		num_pages_makeup = len(response.xpath('//div[@class="results-pagination"]/a').extract()) - 2

		# Our focus is haircare but we want to extract other categories as well
		haircare_urls = ['https://www.lorealparisusa.com/products/hair-care/shop-all-products.aspx?size=20&page={}'.format(x) for x in range(1, num_pages_haircare + 1)]

		skincare_urls = ['https://www.lorealparisusa.com/products/skin-care/shop-all-products.aspx?size=20&page={}'.format(x) for x in range(1, num_pages_skincare + 1)]

		makeup_urls = ['https://www.lorealparisusa.com/products/makeup/shop-all-products.aspx?size=20&page={}'.format(x) for x in range(1, num_pages_makeup + 1)]


		result_urls = haircare_urls + skincare_urls + makeup_urls

		for url in result_urls:
			# For debugging
            # print('='*55) 
            # print(url)
            # print('='*55)
            # Just like request.get(url) which gives a response object
			yield Request(url = url, callback = self.parse_result_page)







