#!/usr/bin/python

# Given some arbitrary text file, display the frequency in which all words are used.
# The text used can be found here: https://www.cs.cmu.edu/~rgs/oz-1.html 

import re
# I assume the file is locally stored
f = open("./resources/the-cyclone.txt", "r")

# "There's" would count as two words
# I choose rexep cause I believe it's the simplest to define a word - one also easily can 
# adjust it if the therm "word" is differently understood
words = re.findall("[A-Za-z]+", f.read()) 

wordcount = {}

for word in words:
    word = word.lower() # we don't care about the capitalization, still is the same word
    if wordcount.get(word):
        wordcount[word] = wordcount[word]+1
    else:
        wordcount[word] = 1

wordcount = {key: value for key, value in sorted(wordcount.items(), key=lambda item: item[1])}
for key, value in wordcount.items():
    print("{:<15}: {:<4}".format(key, value))