import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

print(soup.title)

a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))