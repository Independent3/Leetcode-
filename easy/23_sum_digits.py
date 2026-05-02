#Given a number, return the sum of its digits.

number = 12345

def number_to_string1(number):
    sum = 0
    l22 = []
    number = str(number)
    for i in range(0,len(number)):
        l22.append(number[i])
    for i in range(0,len(l22)):
        sum = sum + int(l22[i])
    return sum
print(number_to_string1(number))


#option 2 - simpler - no list is needed
"""

def sum_digits(number):
    total = 0
    for char in str(number):
        total += int(char)
    return total
    
"""