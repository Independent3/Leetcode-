#Given a sentence, print the most frequent word.


sentence = "the cat sat on the mat the cat"


#need to .split() to make each word seperate like a list
#create dict to keep the frequency count of the words
d = dict()

for x in sentence.split():
    d[x] = d.get(x, 0) + 1
print(max(d, key=d.get))

#for max frequency --> print(max(d.values()))