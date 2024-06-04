import csv
from bs4 import BeautifulSoup
import requests
import datetime

BASE_URL = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=1'

# kospi, kosdaq데이터를 받아서 csv파일로 저장하는 함수
def save_to_csv(kospi_data, kosdaq_data):
    # 컬럼명
    fieldnames = ['N', '종목명', '현재가', '전일비', '등락률', '액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE', '토론실']
    
    # 현재 시간
    current = datetime.datetime.now().strftime('%Y%m%d%H%M')  

    # csv파일로 저장
    with open(f'{current}_KOSPI.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames) # DictWriter 객체 생성
        writer.writeheader()                                 # 컬럼명 쓰기
        writer.writerows(kospi_data)                         # 데이터 쓰기

    with open(f'{current}_KOSDAQ.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kosdaq_data)

# html을 받아서 table을 반환하는 함수
def get_table(soup):
    div = soup.find('div', class_='box_type_l')
    table = div.find('table', class_='type_2')
    return table

# table에서 컬럼과 데이터를 추출하는 함수
def get_table_data(table):
    columns = []
    thead = table.find('thead')
    if thead:                               # thead가 있으면 컬럼명을 추출  
        for th in thead.find_all('th'):     # 컬럼명을 columns에 저장 
            columns.append(th.text.strip()) # strip()을 사용하여 공백 제거

    rows = []
    tbody = table.find('tbody')
    if tbody:                                # tbody가 있으면 데이터를 추출         
        for tr in tbody.find_all('tr'):      # 각 행을 추출
            row = []    
            for td in tr.find_all('td'): # 각 행의 데이터를 추출
                row.append(td.text.strip())  # 데이터를 row에 저장
            rows.append(row)                 # row를 rows에 저장
    return columns, rows


# 크롤링을 할 함수 BASE_URL, PAGE_FROM, PAGE_TO를 인자로 받음
def crawler(BASE_URL, PAGE_FROM, PAGE_TO):  
    start_time = datetime.datetime.now()    # 크롤링 시작 시간
    market_cap = BASE_URL.split('&page')[0] # 시가총액 페이지 base url을 저장

    kospi = []
    kosdaq = []

    for page in range(PAGE_FROM, PAGE_TO+1):                                # PAGE_FROM부터 PAGE_TO까지 크롤링
        kospi_response = requests.get(f'{market_cap}sosok=0&page={page}')   # 코스피 페이지 요청

        kospi_soup = BeautifulSoup(kospi_response.text, 'html.parser')      # BeautifulSoup 객체 생성 (html가져옴)
        kospi_table = get_table(kospi_soup)                                 # html에서 table을 가져옴
        kospi_columns, kospi_rows = get_table_data(kospi_table)             # table에서 컬럼과 데이터를 추출
        for row in kospi_rows:                                              # 데이터를 row에 저장
            kospi.append(dict(zip(kospi_columns, row)))                     # row를 columns와 zip하여 dict로 저장

        kosdaq_response = requests.get(f'{market_cap}sosok=1&page={page}')  # 코스닥 페이지 요청, 이하 동일
        
        kosdaq_soup = BeautifulSoup(kosdaq_response.text, 'html.parser')
        kosdaq_table = get_table(kosdaq_soup)
        kosdaq_columns, kosdaq_rows = get_table_data(kosdaq_table)
        for row in kosdaq_rows:
            kosdaq.append(dict(zip(kosdaq_columns, row)))  


    save_to_csv(kospi, kosdaq)  # csv파일로 저장

    end_time = datetime.datetime.now()      # 크롤링 종료 시간
    elapsed_time = end_time - start_time    # 크롤링 소요 시간
    print(f"Crawling and saving completed successfully in {elapsed_time.total_seconds()} seconds.")



try:
    crawler(BASE_URL, 1, 2)
    print("Success: Crawling and saving completed.")
except Exception as e:
    print("Error: ", e)
