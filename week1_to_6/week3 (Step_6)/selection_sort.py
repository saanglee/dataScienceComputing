"""
ssort0([3, 5, 4, 2])
-> [2] + ssort0([3, 5, 4]) 
-> [2] + [3] + ssort0([5, 4])
-> [2] + [3] + [4] + ssort0([5])
-> [2] + [3] + [4] + [5] + ssort0([])

주의: s.remove(x)가 리스트를 리턴해주는 것이 아님!!, 리스트 s 중에서 가장 앞에 나온 x를 제거하기만 하는 역할
"""

arr = [3, 5, 4, 2]

def ssort0(s):
  if s != []:
    smallest = min(s)
    s.remove(smallest)
    return [smallest] + ssort0(s)
  else:
    return []

# print('ssort0: ',ssort0(arr)) # [2, 3, 4, 5]

def ssort0_desc(s):
  if s != []:
    largest = max(s)
    s.remove(largest)
    return [largest] + ssort0_desc(s)
  else:
    return []

# print('ssort0_desc: ',ssort0_desc([3, 5, 4, 2])) # [5, 4, 3, 2]

### 꼬리 재귀로 소팅 ###

def ssort1(s):
  def loop(s, acc):
    if s != []:
      # print(s, acc)
      smallest = min(s)
      s.remove(smallest)
      # print("after remove smallest: ", s, acc+[smallest])
      return loop(s, acc + [smallest])
    else:
      return acc
  return loop(s, [])

# print('ssort1: ',ssort1(arr)) # [2, 3, 4, 5]

### append 사용해서 소팅 ###

def ssort2(s):
  def loop (s, acc):
    if s != []:
      smallest = min(s)
      s.remove(smallest)
      acc.append(smallest)
      return loop(s, acc)
    else:
      return acc
 
 ### while문 사용해서 소팅 ###
def ssort3(s):
  acc =[]
  while s != []:
    smallest = min(s)
    s.remove(smallest)
    acc.append(smallest)
  return acc

# print("ssort3: ", ssort3([3, 45, 6, 3, 1])) 

# ===================================================

### for문 ###
def ssort4(s):
  print('s: ', s)
  n = len(arr)
  for i in range(n):
    min_idx = i # 현재 위치 = 최소값
    # 현재 위치 다음부터 배열 끝까지 최소값 탐색
    for j in range(i+1, n):
      print('i: ',i, ', min_idx: ', min_idx)
      if arr[j] < arr[min_idx]:
        min_idx = j
    # 찾은 최소값을 현재 위치로 이동
    print('arr[i]: ', arr[i], ', arr[min_idx]: ', arr[min_idx])
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

ssort4([4,2])

def ssort4_desc(s):
  n = len(arr)
  for i in range(n):
    max_idx = i 
    for j in range(i+1, n):
      if arr[j] > arr[max_idx]:
        max_idx = j
      arr[i], arr[max_idx] = arr[max_idx], arr[i]
  return arr