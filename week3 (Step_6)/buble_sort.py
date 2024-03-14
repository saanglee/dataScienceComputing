"""
  리스트에서 인접한 두 수를 비교하여 순서가 바뀐 경우 이를 교환하여 정렬
  제자리 정렬 in-place sort
  - 추가 공간을 사용하지 않고 자체적으로 값을 교환 정렬
  - 리스트 내부에서 수의 교환이 필요, 그래서 추가 공간이 필요하지 않음, 그래서 제자리정렬
  - 선택, 삽입, 합병, 퀵정렬은 제자리 정렬이 아님 (메모리 추가적으로 필요)
"""
  
def bouble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

arr = [3, 1, 9, 5]
print(bouble_sort(arr)) # [1, 3, 5, 9]