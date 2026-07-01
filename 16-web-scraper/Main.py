import requests, sys
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, ConnectionError

url = 'https://books.toscrape.com/'

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('h3')

    if not books:
        sys.exit('No books found on the page')

    print('Book are:')

    for count, book in enumerate(books, start=1):
        print(f'\t{count}. {book.get_text() if book else "There are no books"}')

except HTTPError as http_err:
    if response.status_code == 404:
        sys.exit('HTTP Error 404: Web page not found')
    else:
        sys.exit(f'HTTP Error: {http_err}')

except ConnectionError as conn_err:
    sys.exit(f'Connection Error: {conn_err}')

except requests.exceptions.RequestException as err:
    sys.exit(f'Request failed: {err}')