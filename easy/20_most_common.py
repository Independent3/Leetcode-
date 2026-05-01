#Given a list, find and print the most common element.

numbers = [1, 3, 2, 3, 4, 3, 2, 1, 3]

d = dict()
for x in numbers:
    d[x] = d.get(x, 0) + 1
print(max(d, key=d.get))