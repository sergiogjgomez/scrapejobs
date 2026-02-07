from typing import Dict

DATA_URLS: Dict = {
    "uclahealth": {
        "name": "uclahealth",
        "allowed_domains": ["uclahealth.avature.net"],
        "start_urls": ["https://uclahealth.avature.net/careers/SearchJobs/?jobRecordsPerPage=6&jobOffset=0"],
        "pagination_param": "jobOffset",
        "pagination_step": 6
    },
    "bloomberg": {
        "name": "bloomberg",
        "allowed_domains": ["bloomberg.avature.net"],
        "start_urls": ["https://bloomberg.avature.net/careers/SearchJobs/?jobRecordsPerPage=6&jobOffset=0"],
        "pagination_param": "jobOffset",
        "pagination_step": 6
    },
    "ally": {
        "name": "ally",
        "allowed_domains": ["ally.avature.net"],
        "start_urls": ["https://ally.avature.net/careers/SearchJobs/?jobRecordsPerPage=6&jobOffset=0"],
        "pagination_param": "jobOffset",
        "pagination_step": 6
    }
}