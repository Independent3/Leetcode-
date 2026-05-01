#Given a list of words, print how many words start with a vowel (a, e, i, o, u).


words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
count = 0
for word in words:
    if word.startswith(('a', 'e', 'i', 'o', 'u')):
        count = count + 1

print(count)


"""
#2nd option

words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for word in words:
    if word[0] in vowels:
        count = count + 1
print(count)
"""