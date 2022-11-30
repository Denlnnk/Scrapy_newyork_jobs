import scrapy
from scrapy_playwright.page import PageMethod
from ..items import ScrapyNewyorkJobsItem


class NewyorkJobsSpider(scrapy.Spider):
    name = 'newyork_jobs'

    def start_requests(self):
        yield scrapy.Request('https://newyork.craigslist.org/search/mnh/jjj',
                             meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_methods=[
                                     PageMethod("wait_for_selector", 'div.thumb-result-container')
                                 ]
                             ),
                             errback=self.errback,
                             )

    async def parse(self, response, **kwargs):
        page = response.meta["playwright_page"]
        await page.close()

        for job in response.css('div.thumb-result-container'):
            job_url = job.css('a::attr(href)').get()
            yield scrapy.Request(job_url, callback=self.parse_job)

    def parse_job(self, response):
        job_item = ScrapyNewyorkJobsItem()

        job_item['job_title'] = response.xpath('/html/body/section/section/section/div[1]/p/span[3]/b/text()').get()
        job_item['comprensation'] = response.xpath('/html/body/section/section/section/div[1]/p/span[1]/b/text()').get()
        job_item['employment_type'] = response.xpath(
            '/html/body/section/section/section/div[1]/p/span[2]/b/text()').get()
        yield job_item

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
