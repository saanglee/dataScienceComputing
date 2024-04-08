import os
# print("Current Working Directory: ",os.getcwd()) # 현재 디렉토리
os.chdir('/Users/sangji/Documents/Grad/Spring 2024/Data Science Computing/week4/test') # Change the current working directory to where your file is located

def selection_sort_desc(arr):
    for i in range(len(arr)):       
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def binary_search_rank(arr, avg_score):
    # start : 초기는 0으로 설정
    # end : 초기값은 arr의 length 값으로 설정
    start = 0
    end = len(arr)
    closest_rank = len(arr) + 1 

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == avg_score:
            return mid + 1  
        elif arr[mid] < avg_score:
            end = mid - 1
            closest_rank = mid + 1
        else:
            start = mid + 1
            closest_rank = mid + 2

    return closest_rank



#### Your Code Here ####
# 파일 불러오기 코드 작성
# scores : score.txt 파일에서 읽어온 전체 학생들의 평균 점수를 저장하는 list


scores = []
with open('score.txt', 'r') as score_file:
    for line in score_file:
        scores.append(float(line.strip()))

# 성적 리스트 내림차순 정렬
sorted_scores = selection_sort_desc(scores)

# 사용자로부터 성적 입력 받음
my_score = list(map(float, input('Input your mid score and final score: ').split()))
my_avg = sum(my_score) / 2

# 순위 찾기
rank = binary_search_rank(sorted_scores, my_avg)

print(f"Your rank is: {rank}")
