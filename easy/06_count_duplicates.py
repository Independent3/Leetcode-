#Given a list of numbers, print only the numbers that appear more than once.

numbers = [1, 2, 3, 2, 4, 3, 5, 1]
seen = set()
already_printed = set()

for x in numbers:
    if x in seen and x not in already_printed:
        print(x)
        already_printed.add(x)
    else:
        seen.add(x)
