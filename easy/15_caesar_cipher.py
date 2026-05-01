#Given a string and a shift number,
# encode the string by shifting each letter by the shift number.
# Non-letter characters stay the same.

sentence = "hello world"
shift = 3
result = ""

for char in sentence:
    if char.isalpha():
        result = result + chr(ord(char) + shift)
    else:
        result = result + char

print(result)