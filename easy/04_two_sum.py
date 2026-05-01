#Given a list of numbers and a target, return the two numbers that add up to the target.


numbers = [2, 7, 11, 15]
target = 9
seen = set()

for x in numbers:
    if target - x in seen:
        print(x, target-x)
    else:
        seen.add(x)

