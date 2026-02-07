import scrapy
import re
from typing import List, Dict

from scrapejobs.utils.functions import build_next_offset_url, get_key_value

class GeneralSpider(scrapy.Spider):

    def __init__(self, 
                 name: str, 
                 allowed_domain: List, 
                 start_urls: List,
                 pagination_param: str,
                 pagination_step: int,
                 *args, 
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.allowed_domains = allowed_domain
        self.start_urls = start_urls
        self.pagination_param = pagination_param
        self.pagination_step = pagination_step

    def parse(self, response):
        try:
            elements = response.css("div.article__header")
            for elem in elements:
                
                a = elem.css("a")
                href = a.attrib.get("href")
                if href:
                    yield response.follow(href, self.parse_job)

            pags = response.css("div.list-controls__text__legend").get()
            match = re.search(r"(\d+)-(\d+)\s+of\s+(\d+)", pags)

            if match:
                _, end, total = map(int, match.groups())

                if end < total:
                    next_page = build_next_offset_url(response.url, params=self.pagination_param, step=self.pagination_step)
                    yield scrapy.Request(next_page, callback=self.parse)
        except Exception as e:
            self.logger.error(f"Error parsing listing page: {e} for URL: {response.url}")

    def parse_job(self, response):
        try:
            data = get_key_value(response)
            yield data
        except Exception as e:
            self.logger.error(f"Error parsing job details: {e} for URL: {response.url}")    