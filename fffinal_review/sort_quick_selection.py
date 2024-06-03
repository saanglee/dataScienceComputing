def quick_sort(arr):
  if len(arr) < 1:
    return arr
    
  pivot = arr[0]
  (left, right) = partition(pivot, arr[1:])
  return quick_sort(left) + [pivot] + quick_sort(right)

def quick_partition(pivot, arr):
  left, right = [], []
  for x in arr:
    if x <= pivot:
      left.append(x)
    else:
      right.append(x)
    return (left, right)