import random

arr = [3, 4, 7, 9, 11, 23, 54, 76]
print('arr: ', arr)

### 리스트 안에 key가 있는지 없는지 확인 ### 

### SEQUENCE SEARCH ### 

def seq_search_ox_recursive(s, key):
  if s!= []:
    if s[0] == key:
      return True
    else:
      return seq_search_ox_recursive(s[1:],key)
  else:
    return False

print('seq_search_recursive: ', seq_search_ox_recursive(arr, 11)) # True

def seq_search_ox_iterative1(s, key):
  while s!=[]:
    if s[0] == key:
      return True
    else:
      s = s[1:]
    return False
  
print('seq_search_ox_iterative1: ', seq_search_ox_iterative1(arr, 3)) # False

def seq_search_ox_iterative2(s, key):
  for x in s:
    if x == key:
      return True
  return False

### BINARY SEARCH ###

def binary_search(ss, key):
  if ss != []:
    mid = len(ss)//2
    if key == ss[mid]:
      return True
    elif key < ss[mid]:
      return binary_search(ss[:mid], key) # key가 중간값보다 작으면 왼쪽(0번부터 mid까지)을 다시 탐색
    else:
      return binary_search(ss[mid+1:], key) # key가 중간값보다 크면 오른쪽(mid+1부터 끝까지)을 다시 탐색
  else:
    return False 
  
print('binary_search: ', binary_search(arr, 11)) # True
      
    
def binary_search_iterative(ss, key):
  while ss != []:
    mid = len(ss)//2
    if key == ss[mid]:
      return True
    elif key < ss[mid]:
      ss = ss[:mid]
    else:
      ss = ss[mid+1:]
  return False


### 리스트 안에 key가 어느 위치에 있는지 확인 ###

### SEQUENCE SEARCH ###

def seq_search(s, key):
  i = 0 # counter
  for x in s:
    if x == key:
      # return 'key의 index는 ' + str(i)
      return f"key({key})의 index는 {i}"
    i += 1
  return None

print('seq_search: ', seq_search(arr, 11)) # 4

def bin_search(ss, key):
  low = 0
  high = len(ss) - 1
  while low <= high:
    mid = (low + high) // 2
    if key == ss[mid]:
      # return mid
      return f"key({key})의 index는 {mid}"
    elif key < ss[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return None

print('bin_search: ', bin_search(arr, 23)) # 4