#Given two strings, check if they are anagrams of each other (same letters, different order).
# Print True or False.


word1 = "listen"
word2 = "silent"

word3 = "hello"
word4 = "world"

#anagrams --> dictionary , values + frequency

d1 = dict()
d2 = dict()
d3 = dict()
d4 = dict()

for x in word1:
    d1[x] = d1.get(x, 0) + 1
for x in word2:
    d2[x] = d2.get(x, 0) + 1
if d1 == d2:
    print("True")
else:
    print("False")

for x in word3:
    d3[x] = d3.get(x, 0) + 1
for x in word4:
    d4[x] = d4.get(x, 0) + 1
if d3 == d4:
    print("True")
else:
    print("False")


# Better option 2
"""
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
"""

#option 3
"""
def is_anagram(word1, word2):
    d1 = dict()
    d2 = dict()
    for x in word1:
        d1[x] = d1.get(x, 0) + 1
    for x in word2:
        d2[x] = d2.get(x, 0) + 1
    return d1 == d2

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world")) 

"""