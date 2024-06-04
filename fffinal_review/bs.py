import csv
from bs4 import BeautifulSoup
import request
import datetime

URL = ''

def save_to_csv(data):
    fieldnames = ['', '', '']
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M')

    with open(f'{current_time}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def crawler(URL):
    start_time = datetime.datetime.now()

    response = request.get(URL)
    html = BeautifulSoup(response.text, 'html.parser')

    ol_tag = html.find('ol', class_='prod_list')

    