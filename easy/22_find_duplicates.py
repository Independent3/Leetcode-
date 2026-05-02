#Given a list of numbers, return a list of numbers that appear more than once.


numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6]

def findDuplicates(numbers):
    seen = set()
    l1 = list()
    for x in numbers:
        if x not in seen:
            seen.add(x)
        else:
            if x not in l1:   #to not pass doubles in the list we create after
                l1.append(x)
    return l1
print(findDuplicates(numbers))

