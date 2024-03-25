import random 
### OX 문제

### SEQUENTIAL SEARCH
# 재귀
def seq_search_ox_recursive(s, key):
  if s!= []:
    if s[0] == key:
      return True
    else:
      return seq_search_ox_recursive(s[1:],key)
  else:
    return False

# 반복문
def seq_search_ox_iterative1(s, key):
  while s!=[]:
    if s[0] == key: 
      return True
    else: 
      s = s[1:]
  return False

def seq_search_ox_iterative2(s, key):
  for x in s:
    if x == key:
      return True
  return False

### BINARY SEARCH
def bin_search_ox(ss, key):
  if ss!=[]:
    mid = len(ss)//2
    if key == ss[mid]:
      return True
    elif key < ss[mid]:
      return bin_search_ox(ss[:mid], key)
    else:
      return bin_search_ox(ss[mid+1:], key)
  else:
    return False
  
def bin_search_iterative(ss, key):    
  while ss!=[]:
    mid = len(ss)//2
    if key == ss[mid]:
      return True
    elif key < ss[mid]:
      ss = ss[:mid]
    else:
      ss = ss[mid+1:]
  return False

### 리스트 검색: 찾은 위치 알려주기

## SEQUENTIAL SEARCH
def seq_search(s, key):
  i = 0 # counter 필요
  for x in s:
    if x == key:
      return i
    i += 1
  return None

## BINARY SEARCH
def bin_search(ss, key):
  low = 0
  high = len(ss) - 1
  while low <= high:
    mid = (low + high) // 2
    if key == ss[mid]:
      return mid
    elif key < ss[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return None


## TEST CODE
def test_bin_search():
  print("BINARY SEARCH TEST!")
  db = random.sample(range(10000),1000)
  db.sort() # 파이썬 내장 함수 sorting
  for i in range(10):
    key = random.randrange(10000) # 정수 범위 내에서 하나 랜덤 골라줌
    index = bin_search(db, key)
    print(key, "FOUND AT", index)
  
test_bin_search()


