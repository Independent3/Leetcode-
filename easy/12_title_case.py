# Given a sentence
# print it in title case (first letter of every word capitalized) without using .title().

sentence = "hello my name is nikos"
result = ""
for char in sentence.split():
    char = char.capitalize()
    result = result + " " + char
print (result.strip())


#option 2
"""

result = " ".join(word.capitalize() for word in sentence.split())
print(result)

"""
