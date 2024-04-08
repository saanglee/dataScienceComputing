import os 

# print("Current Working Directory: ",os.getcwd()) # 현재 디렉토리
current_dir = os.getcwd()
os.chdir(f"{current_dir}/week4") # Change the current working directory to where your file is located

# 문자열 검색: 파일 입출력
t = open('input.txt', 'r')

# print(t.open(9))
# print(t.open())
# print(t.readline()) # 한줄 다 읽음 (많이 사용됨)
# print(t.readline(2)) # 현재 줄에서 n개의 문자 읽어옴

first_line = t.readline()
print(first_line)

rest_of_lines = t.readlines()
print(rest_of_lines)

t.close()

t2 = open('output.txt','w')
t2.write('Hello, world!')
t2.close()
