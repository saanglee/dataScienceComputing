### LIST ###

odds = [1, 34, 44, 55, 77, 9]
odds2 = odds # 같은 리스트, 두개의 이름

# print(odds) # [1, 34, 44, 55, 77, 9]
# print(odds2) # [1, 34, 44, 55, 77, 9]

odds2[2] = 4

# print(odds) # [1, 34, 4, 55, 77, 9]
# print(odds2) # [1, 34, 4, 55, 77, 9]

odds3 = odds[:] # odds를 복사해 새로운 리스트를 만듦
odds3[2] = 100

# print(odds) # [1, 34, 4, 55, 77, 9]
# print(odds3) # [1, 34, 100, 55, 77, 9]

### TUPLE ###

t = (1, 2, 3)
print(t[0]) # 1
print(t[:2]) # (1, 2)

# t[2] = 5 # TypeError: 'tuple' object does not support item assignment -> IMMUTABLE

### STRING ###

s = "컴퓨터과학"

# s[3] = "공" # TypeError: 'str' object does not support item assignment -> IMMUTABLE

s1 = s
s1 = s1 + "도"

print(s) # 컴퓨터과학
print(s1) # 컴퓨터과학도

### RANGE ###

r = range(5)
print(r) # range(0, 5)

# r[1] = 3 # TypeError: 'range' object does not support item assignment -> IMMUTABLE

print(3 in r) # True
print(range(3, 11, 2))

for i in range(5):
  print(i) # 0 1 2 3 4

for i in range(3, 10):
  print(i) # 3 4 5 6 7 8 9

for i in range(10, 3, -3):
  print(i) # 10 7 4

for i in range(10, 3, -3):
  for j in range (3, 11, 3):
    print(i, j) 
