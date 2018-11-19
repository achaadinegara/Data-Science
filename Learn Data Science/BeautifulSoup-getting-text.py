import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

guido_title = soup.title

print(guido_title)

guido_text = soup.get_text()

print(guido_text)