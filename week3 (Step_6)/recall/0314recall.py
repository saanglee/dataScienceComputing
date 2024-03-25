### INSERT ###

def isort0(s):
  if s != []:
    return insert(s[0], isort0[1:])
  else:
    return []

def insert(x, sorted_list):
  if not sorted_list: return [x]
  else:
    first = sorted_list[0]
    others = sorted_list[1:]
    if x <= first:
      return [x] + sorted_list
    else:
      return [first] + insert(x, others)

### MERGE ###

def merge0(left, right):
  if not ((left==[]) or (right==[])):
    if left[0] <= right[0]:
      return [left[0]] + merge0(left[1:], right)
    else:
      return [right[0] + merge0(left, right[1:])]
  else:
    left + right

def merge_sort(arr):
  if len(arr) <= 1: return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  return merge0(left, right)

def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[i]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  result += left[i:]
  result += right[j:]
  return result


list = [3, 1, 9, 5]
sorted_list = merge_sort(list)
print(sorted_list) 

### SELECTION ###

def ssort0(s):
  if s != []:
    smallest = min(s)
    s.remove(smallest)
    return [smallest] + ssort0(s)

def ssort1(s):
  def loop(s, acc):
    if s != []:
      smallest = min(s)
      s.remove(smallest)
      return loop(s, acc+[smallest])
    else:
      return acc
  return loop(s, [])


### QUICK ###
def qsort(s):
  if len(s) > 1:
    pivot = s[0]
    (left, right) = partition(pivot, s[1:])
    return qsort(left) + [pivot] + qsort(right)
  else:
    return s

def partition(pivot, s):
  left, right = [], []
  for x in s:
    if x <= pivot:
      left.append(x)
    else:
      right.append(x)
  return (left, right)