# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LorealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subname = scrapy.Field()

    name = scrapy.Field()

    price = scrapy.Field()

    rating = scrapy.Field()

    description = scrapy.Field()

    category = scrapy.Field()

    num_reviews = scrapy.Field()

    main_category = scrapy.Field()
