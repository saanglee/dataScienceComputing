r = list(range(10))

print(type(r)) # <class 'list'>

print(r) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(r[1:8:2]) # [1, 3, 5, 7]

print(len(r)) # 10
print(min(r)) # 0
print(max(r)) # 9

l = [1,2,2,4,2]
print(l.count(2)) # 3