# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyNewyorkJobsItem(scrapy.Item):
    job_title = scrapy.Field()
    comprensation = scrapy.Field()
    employment_type = scrapy.Field()

