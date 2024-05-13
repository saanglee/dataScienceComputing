import numpy as np
import pandas as pd

series_example = pd.Series([100, 50, 30, 10, np.NAN])
# print(series_example)
# print(series_example.index) # RangeIndex(start=0, stop=5, step=1)
# print(series_example.values)
print(series_example.isna())

# 인덱스 바꾸기 1
# series_example.index = ['A', 'B', 'C', 'D', 'E'] 

# 인덱스 바꾸기 2
data = [100, 50, 30, 10, np.NAN]
series_example = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
# print(series_example)

# pandas - dataframe

mid_term = {'student1': 85, 'student2': 99, 'student3': 75, 'student4': 65}
mid_term_series = pd.Series(mid_term)
print('### MIDTERM RESULT ###')
print(mid_term_series)


# 과제 점수나 기말고사 점수 추가하고 싶을 때 -> 2차원 기반 dataframe활용

student_se = pd.Series(['student1', 'student2', 'student3', 'student4'])
mid_term_se = pd.Series([85, 99, 75, 65])
final_term_se = pd.Series([86, 98, 76, 64])

# df = pd.DataFrame(data={'mid_term': mid_term_se, 'final_term': final_term_se}, index=student_se)
df = pd.DataFrame({'Name': student_se, 'Midterm': mid_term_se, 'Final': final_term_se})
print('### MIDTERM & FINAL RESULT ###')
print(df)

# 중간고사 평균값과 가장 높은 점수 출력
# max_level = np.argmax(df['Midterm'])
max_level = np.argmax(mid_term_se)
print('중간고사 점수가 높은 학생:', student_se[max_level])
# print('중간고사 최고점:', mid_term_se[max_level])
print('중간고사 최고점:', mid_term_se.max())
print('중간고사 평균:', mid_term_se.mean())