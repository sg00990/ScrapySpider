
# Name(s): Sarah Graddy & April Breedlove
# Class: CS 4422
# Assignment #: 1

# table1.py creates a table with the categories rank, word, frequency, & percent for the data obtained in the file output.json (w/ stop words)
# It also create two graphs to display that data

# so many imports :O
from collections import Counter
from os import truncate
from tabulate import tabulate
import pandas as pd
import json
import sys
import operator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# counter object
cnt = Counter()

rec = {}

body_length = 0
r = {}

# headers for table
head = ["Rank","Term & Freq.", "Perc."]

# opens json file
file_name = sys.argv[1]
f = open(file_name)
data = json.load(f)

# changes words to lowercase & adds frequencies to counter
with open(file_name) as f:
    data = json.loads(f.read())
    for rec in data:
        rec['body'] = rec['body'].lower()
        cnt.update(rec['body'].split())


# calculates percentage (frequency/total)
percent = [round(cnt[i]/sum(cnt.values()), 3) for i, count in cnt.most_common(30)]



# joins the two data sets to the same table
table = {
    "Term & Freq.": cnt.most_common(30),
    "Perc.": percent 
}

# load table data
df = pd.DataFrame(table)


# prints table, tabulate provides nicer output
print(tabulate(df, tablefmt='fancy_grid', headers=head))

#-------------------------------------------------------------
# Word Dist. Graph

mostCommon = {}


# gets ranking from cnt.most_common(); UNUSED (but should probably go on x-axis somehow)
ranking = {pair[0]: rank 
           for rank, pair in enumerate(cnt.most_common(30))}

# Gets most common word frequencies
mostCommon = [cnt[i] for i, count in cnt.most_common()]

y = mostCommon
x = range(30671)

plt.title("Word Distribution")
plt.xlabel("Rank")
plt.ylabel("Frequency")

plt.plot(x,y)

plt.xlim = 9000

plt.show()


#------------------------------
# Log Graph

m = mostCommon


plt.ylabel("Log Occurances")
plt.xlabel("Rank")

plt.xscale('log')
plt.yscale('log')

plt.plot(range(1, len(mostCommon) + 1), m)

plt.show()

