#!/usr/bin/python

# Given some arbitrary text file, display the frequency in which all words are used.
# The text used can be found here: https://www.cs.cmu.edu/~rgs/oz-1.html 

import re
from urllib.request import urlopen

def wordcount_localfile(file):
    f = open(file, "r")
    wordcount(f.read())

def wordcount_url(url):
    body = urlopen(url).read().decode("utf8")
    text = re.sub(r'<.*?>', '', re.findall(r'<body>((.|\s)*)<\/body>', body, re.IGNORECASE)[0][0], 0, re.IGNORECASE)
    wordcount(text)

def wordcount(text):
    """
    Counts the words of a text using rexep cause I believe it's the simplest to define a word - 
    one also easily can  adjust it if the therm "word" is differently understood
    's is currently count separate though it may be 'is' or the shows possesion like "Dorothy's"
    This is hard to easily distinguish.
    """
    words = re.findall("[A-Za-z]+", text)

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


# I assume the file is locally stored
filename = "./resources/the-cyclone.txt"
wordcount_localfile(filename)

url = "https://www.cs.cmu.edu/~rgs/oz-1.html"
wordcount_url(url)