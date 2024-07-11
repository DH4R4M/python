Simple Web Crawler in Python

This repository contains a simple web crawler implemented in Python. The crawler fetches web pages starting from a base URL and extracts email addresses from those pages.

Features:
- Crawls web pages starting from a base URL.
- Extracts and prints email addresses found on the pages.
- Follows links to a specified maximum depth.
- Only follows links within the same domain as the base URL.

Requirements:
- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip: `pip install requests beautifulsoup4`

Usage:

To use the web crawler, run the `web_crawler.py` script. You can specify the base URL and the maximum depth for crawling.

Replace `https://example.com` with the URL you want to crawl.
