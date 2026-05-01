#Print numbers from 1 to 20. But for multiples of 3 print "Fizz",
# for multiples of 5 print "Buzz",
# and for multiples of both print "FizzBuzz"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #--> for number in range(1,21)
                                                               #-->     if number ....
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
