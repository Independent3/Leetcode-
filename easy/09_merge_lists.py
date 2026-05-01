#Given two lists
# merge them into one list containing only unique values, sorted in ascending order.

list1 = [3, 1, 4, 1, 5]
list2 = [9, 2, 6, 5, 3]


list3 = sorted(list(set(list1 + list2)))
print(list3)



#.sort() returns None