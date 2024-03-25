def merge0(left, right):
  if not ((left==[]) or (right==[])):
    if left[0] <= right[0]:
      return [left[0]] + merge0(left[1:], right)
    else:
      return [right[0] + merge0(left, right[1:])]
  else:
    return left+right
  
### ----- MERGE SORT EXAMPLE ----- ###

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  
  left = merge_sort(left)
  right = merge_sort(right)

  return merge(left, right)

def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]: # left가 더 작을 때
      result.append(left[i])
      i += 1
    else: # right가 더 작을 때
      result.append(right[j])
      j += 1
  
  print('result:', result, 'left[i:]', left[i:], 'right[j:]', right[j:])
  result += left[i:]
  result += right[j:]
  return result


list = [21, 3, 1, 9, 5, 6]
sorted_list = merge_sort(list)
print(sorted_list)