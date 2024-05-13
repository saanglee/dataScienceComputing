import random
import string
import pandas as pd

random.seed(100)


def write_file(resident_list, names, st_address):
    # resident_list를 resident.txt 파일에 저장
    residents = open('resident.txt', 'w')
    for name in resident_list:
        residents.write(name + '\n')

    # 주민 목록(names)과 주소(st_address)를 address.txt 파일에 저장
    address = open('address.txt', 'w')
    for name, address in zip(names, st_address):
        address.write(name + ': ' + address + '\n')
    
    residents.close()
    address.close()

def read_file():
    #### Your Code Here ####
    # 실제 거주민 목록 resident.txt와 저장된 주소록 파일 address.txt불러옴
    residents = open('resident.txt', 'r')
    address = open('address.txt', 'r')
    for line in address: 
        name, addr = line.split(':')
        # 저장된 주소록에서 실제 거주민이 아닌 경우 Not in resident list를 출력
        if name not in residents:
            print('Not in resident list')
        # 저장된 주소록에서 주소가 잘못 입력된 경우 Wrong address를 출력
        elif addr not in address:
            print('Wrong address')
        # 저장된 주소록에서 실제 거주민 & 올바른 주소 -> In resident list and correct address 를 출력
        else:
            print('In resident list and correct address')
        # 각 거리에 사는 거주민의 수 출력 ???

    residents.close()
    address.close()



def random_create(all_names, street_list):
    #### Your Code Here ####
    # 이름 무작위 추출 및 랜덤 주소 생성
    # names : 모든 주민 주소, len(names) == 500
    # resident_list : 실제 거주민 주소, len(resident_list) == 300
    # rand_address : 랜덤으로 생성한 주소, len(rand_address) == 500
    
    # 1. all_names에서 500개 무작위 추출해 names로 저장
    names = random.sample(all_names, 500)
    # 2. 500 중 300(resident_list)을 추출, 실제 거주 주민 이름 resident_list / 500 중 200은 거주하지 않지만 잘못 포함된 사람들
    resident_list = random.sample(names, 300) 
    
    # 3. 주어진 거리명 street_list에서 100을 무작위 추출
    rand_address = []
    random_streets = random.sample(street_list, 100) 
    # 3. 네자리 숫자 무작위 추출해 거리 명에 더해줌
    random_four_num = f"{random.randint(0, 9999):04d}" 
    for street in random_streets:
        rand_address.append(street + ' ' + random_four_num)
    
    # 4. 생성한 주소 중 일부를 숫자 뒤에 알파벳 네개 추가해 틀린 주소 생성
    wrong_address = []
    random_num = random.randint(10, 200)
    random_letters = ''.join(random.choices(string.ascii_letters, k=4))
    
    for address in random.sample(rand_address, random_num):
        wrong_address.append(address + ' ' + random_letters)


    return names, resident_list, rand_address

#### Your Code Here ####
# all_names : names.txt 파일에서 읽어온 모든 이름을 저장한 list

path = 'week4/test/Street_Names.csv' # Street_Names.csv 가 저장된 경로를 넣어주세요

########################

street_nm = pd.read_csv(path)
street_list = street_nm['FullStreetName'].values.tolist()

