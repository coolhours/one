import requests

from bs4 import BeautifulSoup

url = ''

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.string)
