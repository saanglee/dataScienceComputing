import requests
from bs4 import BeautifulSoup

keyword = ''

raw = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + keyword).text
html = BeautifulSoup(raw, 'html.parser')

