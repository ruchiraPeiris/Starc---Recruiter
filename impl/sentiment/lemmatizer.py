from nltk.stem import LancasterStemmer
from pprint import pprint

stemmer = LancasterStemmer()

print(stemmer.stem('communicator'))

file = open('positivewords.txt')

stems = set()
for line in file:
    words = line.split(',')
    for word in words:
        stems.add(stemmer.stem(word))

slist = list(stems)
slist.sort()
print(slist)

