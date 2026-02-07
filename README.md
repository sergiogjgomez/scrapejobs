# ScrapeGlobalJobs 🌍

A global job offers web scraper built with **Scrapy**. This project allows you to extract job data, including details such as location, employment type, department, and related information, saving the results in CSV files.

## Features ✨

- 🕷️ **Web Scraping with Scrapy**: Robust and scalable architecture for data scraping
- 📄 **Automatic Pagination**: Intelligent offset-based pagination handling
- 💾 **CSV Export**: Automatic saving of extracted data
- 🔧 **Flexible Configuration**: Customizable parameters for different sites
- 🛡️ **robots.txt Compliance**: Follows responsible scraping rules
- 📊 **Structured Extraction**: Retrieves key-value fields from job offers

## Requirements

- Python 3.7+
- Scrapy
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd scrapejobs
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or on Linux/Mac: source venv/bin/activate
```

3. Install dependencies:
```bash
pip install scrapy
```

## Usage

### Basic Execution

To run the scraper with the general spider:

```bash
python main.py
```

### Spider Configuration

The `GeneralSpider` accepts the following parameters:

- **name** (str): Identifier name for the spider
- **allowed_domain** (List): Allowed domains for scraping
- **start_urls** (List): Initial URLs to start scraping
- **pagination_param** (str): Name of the pagination parameter (e.g., `jobOffset`)
- **pagination_step** (int): Number of records per page

### Advanced Usage Example

```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapejobs.spiders.general import GeneralSpider

settings = get_project_settings()
process = CrawlerProcess(settings)

spider = GeneralSpider(
    name='jobs_spider',
    allowed_domain=['example.com'],
    start_urls=['https://example.com/jobs'],
    pagination_param='jobOffset',
    pagination_step=20
)

process.crawl(spider)
process.start()
```

## Project Structure

```
scrapejobs/
├── main.py                 # Project entry point
├── requirements.txt        # Project dependencies
├── scrapy.cfg             # Scrapy configuration
├── scrapejobs/
│   ├── __init__.py
│   ├── settings.py        # Scrapy settings
│   ├── items.py           # Item definitions (data models)
│   ├── middlewares.py     # Custom middlewares
│   ├── pipelines.py       # Processing pipelines
│   ├── documents/         # Data output folder
│   │   └── output_2026-02-06.csv
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── general.py     # Main spider
│   └── utils/
│       ├── declarative.py # Declarative utilities
│       └── functions.py   # Helper functions
```

## Main Components

### main.py
Entry point that initializes the `CrawlerProcess` and runs the spider.

### GeneralSpider (spiders/general.py)
Main spider that:
- Traverses job offer pages
- Extracts URLs from individual job listings
- Handles pagination automatically
- Parses detailed information from each job offer

### Helper Functions (utils/functions.py)

#### `build_next_offset_url(url, param_name, step)`
Builds the next pagination URL by incrementing the offset parameter.

#### `get_key_value(response)`
Extracts key-value pairs from HTML response, such as:
- Job Location
- Employment Type
- Department
- Job ID

## Configuration

### settings.py

Important configurations:

- **BOT_NAME**: Bot name (`scrapejobs`)
- **ROBOTSTXT_OBEY**: Respects `robots.txt` rules (enabled by default)
- **CONCURRENT_REQUESTS**: Maximum number of concurrent requests
- **DOWNLOAD_DELAY**: Delay between requests for responsible scraping

## Output

Extracted data is saved in the `documents/` folder in CSV format with timestamps:

```
documents/
└── output_2026-02-06.csv
```

## Best Practices

1. ✅ Always respect `robots.txt` and site policies
2. ✅ Configure appropriate delays between requests
3. ✅ Identify your bot with a descriptive User-Agent
4. ✅ Handle exceptions in data parsing
5. ✅ Monitor scraping activity

## Development

### Creating New Spiders

Place new spiders in `spiders/` inheriting from `GeneralSpider` or `scrapy.Spider`:

```python
class CustomSpider(GeneralSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            name='custom',
            allowed_domain=['example.com'],
            start_urls=['https://example.com'],
            pagination_param='page',
            pagination_step=10,
            *args,
            **kwargs
        )
```

## License

This project is open source. Use it freely while respecting the licenses of dependencies and the policies of the sites you scrape.

## Contributing

Contributions are welcome. Please:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

To report issues or make suggestions, open an issue in the repository.

---

**Built with ❤️ for responsible scrapers**
