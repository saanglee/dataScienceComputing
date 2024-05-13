import os 

current_dir = os.getcwd()
os.chdir(f"{current_dir}/week4/recall") # Change the current working directory to where your file is located

def selection_sort_desc(arr):
  for i in range (len(arr)): 
    # i = 0
    # i = 1
    max_idx = i
    for j in range(i + 1, len(arr)): 
      # j = 1 ➡️ j = 2 ➡️ j = 3 ➡️ j = 4
      # j = 2 ➡️ j = 3 ➡️ j = 4
      if arr[j] > arr[max_idx]: 
        # 45 > 3 ✅ ➡️ 6 > 45 ❌ ➡️ 3 > 45 ❌ ➡️ 1 > 45 ❌
        # 6 > 3 ✅ ➡️ 3 > 6 ❌ ➡️ 1 > 6 ❌ 
        max_idx = j # max_idx = 1 (45)
    arr[i], arr[max_idx] = arr[max_idx], arr[i] 
    # 3, 45 = 45, 3 : [45, 3, 6, 3, 1]
    # 3, 6 = 6, 3 : [45, 6, 3, 3, 1]
  return arr

def binary_search_rank(arr, avg_score):
  # binary_search_rank([100, 99, 90, 44], 70)
  start = 0
  end = len(arr) # 4
  closest_rank = len(arr) + 1 # 5
  
  while start <= end:
    mid = (start + end) // 2 # 1️⃣ mid = 2 # 2️⃣ mid = 3 # mid = 2?
    if mid >= len(arr):
      return mid + 1
    if arr[mid] == avg_score: # 1️⃣ 90 == 70 ❌ # 2️⃣ 44 == 70 ❌ 
      return mid + 1
    elif arr[mid] < avg_score: # 1️⃣ 90 < 70 ❌ # 2️⃣ 44 < 70 ✅
      end = mid - 1 # 2️⃣ end = 2
      closest_rank = mid + 1 # 2️⃣ clo_rank = 3
    else: # 1️⃣ 90 > 70 ✅
      start = mid + 1 # 1️⃣ start = 3
      closest_rank = mid + 2 # 1️⃣ 4
  return closest_rank
    
    
    
scores = []
with open('score.txt', 'r') as score_file:
  for line in score_file:
    scores.append(float(line.strip()))
# print(scores)

sorted_scores = selection_sort_desc(scores)

# my_score = list(map(float, input('MID & FINAL SCORE: ').split()))
# print(my_score)
# my_avg = sum(my_score) / 2

# rank = binary_search_rank(sorted_scores, my_avg)

# print(f"MY RANK IS {rank}")

test = binary_search_rank([100, 99, 90, 44], 14)
print('test: ', test)