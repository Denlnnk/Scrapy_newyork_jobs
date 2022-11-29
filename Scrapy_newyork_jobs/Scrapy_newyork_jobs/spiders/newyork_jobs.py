import scrapy
from scrapy_playwright.page import PageMethod


class NewyorkJobsSpider(scrapy.Spider):
    name = 'newyork_jobs'

    def start_requests(self):
        pass
