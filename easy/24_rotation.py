#Given two strings, check if one is a rotation of the other. Print True or False.


word1 = "abcde"
word2 = "cdeab"
# expected output True

word3 = "abcde"
word4 = "abced"

# expected output False

def checkrotation(word1 , word2):
    word = word1 + word1
    if word2 in word:
        return True
    else:
        return False


print(checkrotation(word1 , word2))