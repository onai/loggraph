import os
import sys
import csv
import pandas
import json
import re


logfilename = sys.argv[1]
threshold = 10

colnames = ['date', 'time', 'def', 'status', 'iph1', 'ip1', 'userh', 'user', 'iph2', 'ip2' ]

delimiters = [' ', '\t', ';']

f2 = open(logfilename)
blot = f2.readline()
f2.close()
delim = ',' # default delimiter

# Simple delim matcher
if re.match(r' *', blot):
    delim = ' *'
elif re.match(r'\t', blot):
    delim = '\t'
elif ';' in blot:
    delim = ';'

data = pandas.read_csv(logfilename, delimiter=delim, names=colnames)

print("Printing rows with delim as " + delim + ":")
print(data.loc[0])

date = data.date.tolist()
time = data.time.tolist()
ip1 = data.ip1.tolist()
status = data.status.tolist()
user = data.user.tolist()
ip2 = data.ip2.tolist()

X = [date, time, ip1, status, user, ip2]

matchlist = []
for ii, i in enumerate(X):
    for jj, j in enumerate(X):
        if ii == jj:
            continue

        if len(set(i).intersection(set(j))) > threshold:
            matchlist.append([i, j])



if not matchlist:
    print("No GRAPH")

# build giraph

# giraph format: [source_id,source_value,[[dest_id, edge_value],...]]
graphcount = 0
for match in matchlist:
    giraph = []
    srcIndices = {}
    counter = 0
    for srcEdge, destEdge in zip(match[0], match[1]):
        if srcEdge not in srcIndices:
            giraph.append([srcEdge, [[destEdge, 1]]])
            srcIndices[srcEdge] = counter
            counter += 1
    
        else:
            indx = srcIndices[srcEdge]
            giraph[indx][1].append([destEdge, 1])
   
    with open(str(graphcount) + '.json', 'w') as outfule:
        json.dump(giraph, outfule)

    graphcount += 1
    
