#Given a list of numbers from 1 to 10 with one number missing, find the missing number.


numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
sorted_numbers = sorted(numbers)

for i in range(0, len(sorted_numbers)):
    if sorted_numbers[i] != i+1:
        print(i+1)
        break
