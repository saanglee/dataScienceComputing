"""
• 주 요 기 능
    1. 학 생 이 고 른 웹 페 이 지 를 입 력 받 을 수 있 어 야 함 .
    2. 입 력 받 은 웹 페 이 지 를 본 인 나 름 대 로 정 한 고 유 한 정 의 를 통 해 분 류 하 고 이 를
        C S V 파 일 로 저 장 하 여 e x p o r t 할 수 있 어 야 함 .
    3. 출 력 C S V 파 일 의 이 름 은 현 재 날 짜 과 시 간 이 포 함 된 C S V 파 일 이 어 야 함
    예 : 현 재 시 간 이 2 0 x x 년 5 월 1 9 일 오 후 3 시 2 0 분 일 경 우 - 2 0 X X 0 5 1 9 1 5 2 0 . c s v
    4 . 완 료 후 에 는 크 롤 링 결 과 와 소 요 시 간 을 안 내 해 주 어 야 함 .
• 주 의 사 항
    1 . 대 상 웹 페 이 지 의 경 우 , 온 라 인 게 시
    2 . 해 당 크 롤 러 의 경 우 , 각 l i n e 이 어 떠 한 역 할 과 동 작 을 하 는 지 주 석 을 쓸 것 .

순위/책 이름/작가/출판사/출판일/가격/평점/리뷰개수
 fieldnames = ['rank', 'title', 'author', 'publisher', 'date', 'price', 'rating', 'review_count']
"""

import csv
from bs4 import BeautifulSoup
import requests
import datetime

URL = 'https://product.kyobobook.co.kr/bestseller/total?period=004#?page=1&per=20&period=004&ymw=&bsslBksClstCode=A'

def save_to_csv(data):
    # csv title =  year+month+day+hour+minute.csv
    fieldnames = ['rank', 'title', 'author', 'publisher', 'date', 'price', 'rating', 'review_count']
    
    current = datetime.datetime.now().strftime('%Y%m%d%H%M')  

    with open(f'{current}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def crawler(URL):
    start_time = datetime.datetime.now()
    print('Start: ', start_time)

    response = requests.get(URL)
    html = BeautifulSoup(response.text, 'html.parser')
    print(html)
    # find ol tag
    ol_tag = html.find('ol', class_='prod_list')
    # print(ol_tag)
    # find all li tags
    # li_tags = ol_tag.find_all('li', class_='prod_item')

    """
    <div class="prod_info_box"><div class="prod_rank"><div class="badge_flag badge_green best"><span class="text"> Best <span class="fw_bold">1</span></span></div></div><div class="prod_badge"><span class="badge_md badge_line_primary rep"><span class="text">MD의 선택</span></span><span class="badge_md badge_line_gray rep"><span class="text">예약판매</span></span><span class="badge_md badge_line_gray rep"><span class="text">이벤트</span></span><span class="badge_md badge_line_gray rep"><span class="text">사은품</span></span><span class="badge_md badge_line_gray rep"><span class="text">소득공제</span></span></div>
  <div class="auto_overflow_wrap prod_name_group">
    <div class="auto_overflow_contents">
      <div class="auto_overflow_inner">
        <a href="https://product.kyobobook.co.kr/detail/S000200746091" class="prod_info">
          
      <span class="prod_label">예약판매</span> 세이노의 가르침
    
        </a>
      </div>
    </div>
  </div>
  <span class="prod_author">세이노(SayNo) ·  데이원  <span class="date"> · 2023.03.02</span></span><div class="prod_price"><span class="percent">10%</span><span class="price"><span class="val">6,480</span><span class="unit">원</span></span><span class="price_normal"><span class="text">정가</span><s class="val">7,200원</s></span><span class="gap">|</span><span class="point">360p</span></div><p class="prod_introduction">2000년부터 발표된 그의 주옥같은 글들. 독자들이 자발적으로 만든 제본서는 물론, 전자책과 앱까지 나왔던 《세이노의 가르침》이 드디어 전국 서점에서 독자들을 마주한다. 여러 판본을 모으고 저자의 확인을 거쳐 최근 생각을 추가로 수록하였다. 정식 출간본에만 추가로 수록된 글들은 목차와 본문에 별도 표시하였다.

더 많은 사람이 이 책을 보고 힘을 얻길 바라기에 인세도 안 받는 저자의  마음을 담아, 700쪽이 넘는 분량에도 7천 원 안팎에 책을 구매할 수 있도록 했다. 정식 출간 전자책 또한 무료로 선보인다.

*필명 ‘세이노(Say No)’는 당신이 믿고 있는 것들에 ‘No!’를 외치고 제대로 살아가라는 뜻이다. 세이노는 지난 20여 년간 여러 칼럼을 통해 인생 선배로서 부와 성공에 대한 지혜와 함께 삶에 대한 체험적 지식을 나누어 주었다. 그래서 그의 글을 좋아하는 사람들은 그를 ‘세이노 스승님’이라 부른다.</p><div class="prod_bottom"><div class="review_summary_wrap type_sm"><span class="review_klover_box"><span class="review_klover_text font_size_xxs">9.27</span><span class="review_desc">(3,462개의 리뷰)</span></span><span class="gap">/</span><span class="review_quotes_text font_size_xxs">도움돼요</span></div></div></div>
    """
    books = []

    # for li in li_tags:
    #     rank = li.find('div', class_='prod_rank').get_text(strip=True)
    #     print(rank)


    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f"Crawling and saving completed successfully in {elapsed_time.total_seconds()} seconds.")


crawler(URL)
# try:
#     crawler(URL)
#     print("Success: Crawling and saving completed.")
# except Exception as e:
#     print("Error: ", e)
