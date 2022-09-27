# Name(s): Sarah Graddy & April Breedlove
# Class: CS 4422
# Assignment #: 1


# table1.py creates a table with the categories rank, word, frequency, & percent for the data obtained in the file output.json (w/o stop words)

# more imports!! :D
from collections import Counter
from os import truncate
from tabulate import tabulate
import pandas as pd
import numpy as np
import string

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

import json
import sys
import operator

# counter object
cnt = Counter()


rec = {}

# headers for graph
head = ["Rank","Term & Freq.", "Perc."]

#opens json file
file_name = sys.argv[1]
f = open(file_name)
data = json.load(f)

# establishes stop words
stopwords = set(stopwords.words('english'))

# add words from file to counter
with open(file_name) as f:
    data = json.loads(f.read())
    for rec in data:
        rec['body'] = rec['body'].lower()
        cnt.update(rec['body'].split())

# if word in counter is a stopword or punctuation, delete
for word in stopwords:
        del cnt[word]
for word in rec['body']:
    if word in string.punctuation:
        del cnt[word]

# calculates percentage (frequency/total)
percent = [round((cnt[i] / sum(cnt.values())), 3) for i, count in cnt.most_common(30)]

# joins the two data sets to the same table
table = {
    "Term & Freq.": cnt.most_common(30),
    "Perc.": percent 
}

# loads table data
df = pd.DataFrame(table)

# prints table, tabulate provides nicer output
print(tabulate(df, tablefmt='fancy_grid', headers=head))

