import csv
from bs4 import BeautifulSoup
import requests


def crawler():
    base_url = 'https://sports.news.naver.com/volleyball/record/index?category='
    
    for year in range(2022, 2024): # 2005, 2024
        url_male = base_url + 'kovo&year=' + str(year)
        url_female =  base_url + 'wkovo&year=' + str(year)

        response_male = requests.get(url_male)
        response_female = requests.get(url_female)

        html_male = BeautifulSoup(response_male.text, 'html.parser')
        html_female = BeautifulSoup(response_female.text, 'html.parser')

        ### get table from html ###
        male_team_table = html_male.find('div', class_='tbl_box').find('table')
        female_team_table = html_female.find('div', class_='tbl_box').find('table')

        male_player_table = html_male.find('div', class_='tbl_box type2').find('table')
        female_player_table = html_female.find('div', class_='tbl_box type2').find('table')

        ### get data from table ### 
        male_team_data = get_data(male_team_table)
        female_team_data = get_data(female_team_table)

        male_player_data = get_data(male_player_table)
        female_player_data = get_data(female_player_table)

        # save team data to CSV
        save_to_csv(male_team_data, f'{year}_man_TeamRecord.csv')
        save_to_csv(female_team_data, f'{year}_woman_TeamRecord.csv')

        # save player data to CSV
        save_to_csv(male_player_data, f'{year}_man_PlayerRecord.csv')
        save_to_csv(female_player_data, f'{year}_woman_PlayerRecord.csv')



def get_data(table):
    player_data = []
    for row in table.find('tbody').find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        player_data.append(row_data)   
    return player_data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)



if __name__ == '__main__':
    crawler()