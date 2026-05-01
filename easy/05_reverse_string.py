#Given a string, print it reversed without using any built-in reverse function.

word = "hello"
result = ""
for char in word:
    result = char + result
print(result)






#print(word[::-1]) --> Built in
# .reverse() only for lists not strings