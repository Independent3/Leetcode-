#Given a list of numbers prin only the numbers that are greater than the average of the list


numbers = [4,8,15,16,23,42]


#prepei na brw to average --> avg = sum(numbers)/len(numbers)
#loop gia print ari8mwn > average


avg = sum(numbers)/len(numbers)


for number in numbers:
    if number > avg:
        print(number)