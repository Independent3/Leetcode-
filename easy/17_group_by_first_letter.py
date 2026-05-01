#Given a list of words, group them by their first letter and print the result.

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]

""" EXPECTED OUTPUT
a: ['apple', 'avocado', 'apricot']
b: ['banana', 'blueberry']
c: ['cherry']

"""

d = dict()
for word in words:
    key = word[0]  # first letter
    if key not in d:
        d[key] = []
    d[key].append(word)

for key, value in d.items():
    print(f"{key}: {value}")




""" Option 2
list1 = list()
list2 = list()
list3 = list()

for word in words:
    if word.startswith("a"):
        list1.append(word)
    elif word.startswith("b"):
        list2.append(word)
    elif word.startswith("c"):
        list3.append(word)
print(f"a: {list1}")
print(f"b: {list2}")
print(f"c: {list3}")
"""
