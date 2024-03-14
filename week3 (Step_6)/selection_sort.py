
list = [3, 5, 4, 2]
def ssort0(s):
  if s != []:

    smallest = min(s)
    s.remove(smallest)
    return [smallest] + ssort0(s) # 재귀를 활용한 반복
  else:
    return []

# print(ssort0(list)) # [2, 3, 4, 5]

"""
ssort0([3, 5, 4, 2])
-> [2] + ssort0([3, 5, 4]) 
-> [2] + [3] + ssort0([5, 4])
-> [2] + [3] + [4] + ssort0([5])
-> [2] + [3] + [4] + [5] + ssort0([])

주의: s.remove(x)가 리스트를 리턴해주는 것이 아님!!, 리스트 s 중에서 가장 앞에 나온 x를 제거하기만 하는 역할
"""

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

print(ssort1(list)) # [2, 3, 4, 5]

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

print("ssort3: ", ssort3([3, 45, 6, 3, 1])) 