import random

def bubble_sort(lcm_list):
    n = len(lcm_list)
    if n == 1:
        return lcm_list
    for i in range(n-1):
      if lcm_list[i] > lcm_list[i+1]:
        lcm_list[i], lcm_list[i+1] = lcm_list[i+1], lcm_list[i]
    lcm_list = bubble_sort(lcm_list[:-1]) + lcm_list[-1:]
    return lcm_list


def insert_sort(lcm_list): 
    ### Edit Here ###
    if lcm_list != []:
        return insert_desc(lcm_list[0], insert_sort(lcm_list[1:]))
    else:
        return []

def insert_desc(x, sorted_list): # 내림차순
    if not sorted_list:
        return [x]
    else:
        first = sorted_list[0]
        others = sorted_list[1:]
        if x >= first:
            return [x] + sorted_list
        else: 
            return [first] + insert_desc(x, others)


def lcm_sort(random_list):
    lcm_list = []
    ### Edit Here ###
    for x in random_list:
        for y in random_list:
            lcm = x * y
            lcm_list.append(lcm)
    return lcm_list




#### Do not edit here ####
random.seed(100)
random_list = random.sample(range(2, 50), 10)

print(f'Initial List is: {random_list}\n')

unsorted_lcmlist = lcm_sort(random_list)

print(f'List of Least Common Multiple is: {unsorted_lcmlist}\n')
ac_sorted = bubble_sort(unsorted_lcmlist)
print(f'Sorted in Ascending Order: {ac_sorted}\n')

dc_sorted = insert_sort(unsorted_lcmlist)
print(f'Sorted in Descending Order: {dc_sorted}\n')
