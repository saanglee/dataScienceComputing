

def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-1-i):
      if arr[j] > arr[j+1]: # desc는 < 
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def bubble_sort_recursive(arr):
  n = len(arr)
  if n == 1:
    return arr
  for i in range(n-1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
  return bubble_sort_recursive(arr[:-1]) + arr[-1:]


def insert_recursive(x, sorted_list):
  if not sorted_list:
    return [x]
  else:
    first = sorted_list[0]
    others = sorted_list[1:]
    if x <= first: # desc는 >= 
      return [x] + sorted_list
    else:
      return [first] + insert_recursive(x, others)

def devide_and_merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid_index = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  left = merge(left)
  right = merge(right)

  return merge_sort(left, right)

def merge_sort(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[i]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[i])
      j += 1