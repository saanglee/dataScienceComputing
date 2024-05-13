# list = [4, 5, 7, 8, 11, 22, 34]
# lcm_list = [] 
# for x in list:
#     for y in list:
#         # get LCM of x and y and store it in lcm
#         lcm = x * y
#         lcm_list.append(lcm)
# print(lcm_list)

#######################

# def calculate_h_index(citations):
#     citations = bubble_sort(citations)
#     n = len(citations)
#     h_index = 0
#     for i in range(n):
#         if citations[i] > i + 1:
#             h_index = i + 1
#         else:
#             break  # No need to continue if citations[i] < i+1
#     return h_index


def calculate_h_index(citations):
    h_index= 0
    citations = bubble_sort(citations)
    for i in citations:
        if i > h_index:
            h_index += 1
          
        
    return h_index

def bubble_sort(list):
    n = len(list)
    if n == 1:
        return list
    for i in range(n-1):
      if list[i] < list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    list = bubble_sort(list[:-1]) + list[-1:]
    return list
  
h_index = calculate_h_index([1,1,3])
print("h_index: ",h_index)

"""
Initial Random List is: [9, 23, 15, 10, 24, 4, 29, 25, 15, 0, 25, 12, 14, 16]
Researcher's h-index is: 10
[1, 21, 29, 9, 12, 19, 20, 30, 12]
[3,0,6,1,5]
def calculate_h_index(citations):
    citations.sort(reverse=True)  # Sort in non-increasing order
    n = len(citations)
    h_index = 0
    for i in range(n):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break  # No need to continue if citations[i] < i+1
    return h_index
"""