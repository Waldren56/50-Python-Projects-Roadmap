# 16 — Simple Web Scraper

A terminal tool that scrapes book titles from [books.toscrape.com](https://books.toscrape.com) and prints them in a numbered list. First project in the series to use external libraries and make real HTTP requests.

## Skills used

- HTTP requests with `requests.get()` and `timeout`
- Response validation with `raise_for_status()`
- Multi-level exception handling: `HTTPError`, `ConnectionError`, `RequestException`
- HTML parsing with `BeautifulSoup` and `find_all()`
- Early exit with `sys.exit()` on empty results or errors

## How to run

```bash
cd 16-web-scraper
uv add requests beautifulsoup4
uv run main.py
```

Requires an active internet connection.