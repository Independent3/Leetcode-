#Given a sentence, count the number of words that contain at least one digit.

sentence = "hello world 123 my name is n1kos and I have 4 cats"

l1 = sentence.split()
count = 0
for word in l1:
    for char in word:
        if char.isdigit():
            count += 1
            break
print(count)
