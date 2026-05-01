#Given a list of tuples, convert it to a dictionary.


pairs = [("name", "Nikos"), ("age", 25), ("city", "Patras")]

# Expected output: {'name': 'Nikos', 'age': 25, 'city': 'Patras'}


d = dict()

for x in pairs:
    d[x[0]] = x[1]
print(d)

#option 2
"""
d = dict(pairs)
"""