import time

print(time.time()) # return the current time in seconds since the epoch
print(time.localtime()) 

for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # 현재 실행 중인 프로그램 1초 동안 정지
print('Blast off!')

