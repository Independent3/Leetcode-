#Given a string, count how many vowels it contains.

sentence = "Hello my name is Nikos"

vowels = ["a", "e", "i", "o", "u"]
count = 0

for x in sentence.split():
    for i in range(0,len(x)):
        if x[i].lower() in vowels:
            count = count + 1
print(count)



""" #Better solution

sentence = "Hello my name is Nikos"
vowels = ["a", "e", "i", "o", "u"]
count = 0

for char in sentence:
    if char.lower() in vowels:
        count += 1
print(count)

"""