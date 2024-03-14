fruits = ['apple', 'banana']
fruits.append('orange')
# print(fruits) 

more_fruits = ['mango', 'watermelon']
fruits.extend(more_fruits)
fruits += more_fruits
# print(fruits) # ['apple', 'banana', 'orange', 'mango', 'watermelon']

# print(fruits[:3]) # 0, 1, 2 번째 인덱스까지
# print(fruits[::2]) # 0, 2, 4 번째 인덱스
# print(fruits[:-1]) # 0부터 맨 마지막 앞까지 
# print(fruits[::-1]) # reverse

# print(fruits.index('orange'))
# print(len(fruits))
# fruits.sort()
# fruits.reverse()
# print(fruits)

numbers = [5, 9, 2, 7, 8, 3, 1, 7, 4, 6]
print(numbers.count(7))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])

numbers2 = [1,2,3,4,5]
squares = [x ** 2 for x in numbers2]
print(squares) # [1, 4, 9, 16, 25]

### Dictionary ###

student_grades = {'Nibedita': 85, 'Tushar': 82, 'Salil': 88, 'Mayukh': 91}
# Let's update Nibedita's grade
student_grades['Nibedita'] = 89

for student, grade in student_grades.items():
  print(student, grade)
  
  
# REMOVING ENTRIES
del student_grades['Salil']
print(student_grades)
