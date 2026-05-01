#Given a nested list, flatten it into a single list.

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


result = []
for i in range(0,len(nested)):
    result.extend(nested[i])
print(result)


"""
not_nested = nested[0] + nested[1] +nested[2]
print(not_nested)
"""