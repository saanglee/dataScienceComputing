def isort0(s):
  if s != []:
    return insert(s[0], isort0(s[1:])) # x, sorted_list
  else:
    return []


### MY INSERT ### 
def insert(x, sorted_list):
  if not sorted_list:
    return [x]
  else:
    first = sorted_list[0]
    others = sorted_list[1:]
    if x <= first:
      return [x] + sorted_list
    else: 
      return [first] + insert(x, others)
    

list = [3, 5, 4, 2, 1, 42, 13, 21]

print(isort0(list))

# Descending Order My Insert
def insert_descending(x, sorted_list):
  if not sorted_list:
    return [x]
  else:
    first = sorted_list[0]
    others = sorted_list[1:]
    if x >= first:
      return [x] + sorted_list
    else: 
      return [first] + insert_descending(x, others)



# def insert(x, sorted_list):
#   if not sorted_list:
#     return [x]
#   else:
#     if x <= sorted_list[0]:
#       return [x] + sorted_list
#     else: # x > sorted_list[0]
#       return [sorted_list[0]] + insert(x, sorted_list[1:])

# def insert(x, sorted_list):
#   for i in range(len(sorted_list)):
#     if x <= sorted_list[i]:
#       return sorted_list[:i] + [x] + sorted_list[i:]
#   return sorted_list+[x]
  