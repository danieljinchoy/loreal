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


		urls = haircare_urls + skincare_urls + makeup_urls

		for url in urls:
			# For debugging
            # print('='*55) 
            # print(url)
            # print('='*55)
			yield Request(url = url, callback = self.parse_result_page)

	def parse_result_page(self, repsonse):
		products = response.xpath('//div[@class="product-container"]')
		
		for product in products:

            try:
                url = 'https://www.lorealparisusa.com' + product.xpath('./a/@href').extract_first()
            except:
                continue


            try:
                product_name = product.xpath('./div[@class="product-container__data"]/div/a/h3/text()').extract_first()
            except:
                product_name = None


            try:
                product_price = product.xpath('./div[@class="product-container__actions"]/a/span/text()').extract_first()
            except:
                product_price = None

            yield Request(url=url, callback=self.parse_detail_page, meta ={'name': product_name, 'price': product_price})


    # Can I parse the review pages using scrapy?

    def parse_detail_page(self, response):
        name = response.meta['name']
        price = response.meta['price']

        # main category
        try:
            main_category = response.xpath('//span[@itemprop="name"]/text()').extract()[1]
        except:
            main_category = None

        # category
        try:
            category = response.xpath('//span[@itemprop="name"]/text()').extract()[3]
        except:
            category = None

        # rating
        try:
            rating = response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first()
        except:
            rating = None

        # number of reviews
        try:
            num_reviews = response.xpath('//span[@itemprop="reviewCount"]/text()').extract_first()
        except:
            num_reviews = None
        
        item = LorealItem()
        item['name'] = name
        item['price'] = price
        item['rating'] = rating
        item['category'] = category
        item['num_reviews'] = num_reviews
        item['main_category'] = main_category

        yield item
