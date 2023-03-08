#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items_sorted = sorted(counts[args.key].items(), key=lambda item: (item[0],item[1]))
for k,v in items_sorted:
    print(k,':',v)

# Create bar plot
for k,v in items_sorted[:10]:
    plt.bar(k, v)

# Set plot title and axis labels
plt.title('Top 10 countries for coronavirus Hashtag')
plt.xlabel('Country')
plt.ylabel('Number of Tweets')

# Save plot as PNG file
plt.savefig('coronavirus_c.png')


# Show plot
plt.show()

