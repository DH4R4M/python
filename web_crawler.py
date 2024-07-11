# web_crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

class SimpleWebCrawler:
    def __init__(self, base_url, max_depth=2):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()
        self.emails = set()

    def crawl(self, url, depth):
        if depth > self.max_depth or url in self.visited:
            return

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return

            self.visited.add(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            self.extract_emails(soup)

            for link in soup.find_all('a', href=True):
                next_url = urljoin(self.base_url, link['href'])
                if self.is_valid_url(next_url):
                    self.crawl(next_url, depth + 1)

        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    def extract_emails(self, soup):
        for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text()):
            self.emails.add(email)

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https') and parsed.netloc == urlparse(self.base_url).netloc

    def get_emails(self):
        return self.emails

if __name__ == "__main__":
    base_url = 'https://example.com'  # Replace with the URL you want to crawl
    crawler = SimpleWebCrawler(base_url)
    crawler.crawl(base_url, 0)
    print("Emails found:")
    for email in crawler.get_emails():
        print(email)
