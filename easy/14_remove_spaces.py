#Given a string,
#remove all extra spaces so there is only one space between words
#and no leading or trailing spaces.

sentence = "  hello   my   name   is   nikos  "
sentence1 = ""
for x in sentence.strip().split():
    sentence1 = sentence1 + " " + x
print(sentence1.strip())


#better option 2

"""
sentence = "  hello   my   name   is   nikos  "
print(" ".join(sentence.split()))
"""