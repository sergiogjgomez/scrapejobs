import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapejobs.utils.declarative import DATA_URLS

from scrapejobs.spiders.general import GeneralSpider

def main(spider):
    base_settings = get_project_settings()
    process = CrawlerProcess(base_settings)
    for spider_name, spider_info in DATA_URLS.items():
        logging.info(f"Starting crawl for {spider_name}")
        process.crawl(spider, **spider_info)
    process.start()
    logging.info("Scraping completed.")

if __name__ == "__main__":
    main(GeneralSpider)

