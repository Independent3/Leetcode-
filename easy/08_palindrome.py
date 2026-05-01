#Given a list of words
# print only the ones that are palindromes (read the same forwards and backwards).

words = ["racecar", "hello", "level", "world", "madam"]

for x in words:
    if x == x[::-1]:
        print(x)
