import sys
import os
import re
import json

# todo:
# 1. edge counter
# 2. port

edges = []
with open(sys.argv[1]) as f:
    for line in f:
        sip = re.findall( r'src: /[0-9]+(?:\.[0-9]+){3}', line )
        dip = re.findall( r'dest: /[0-9]+(?:\.[0-9]+){3}', line )

        if not sip or not dip:
            continue

        edges.append([re.sub(r'src: /', r'', sip[0]), re.sub(r'dest: /', r'', dip[0])])

print("Scanned all edges!")

# giraph format: [source_id,source_value,[[dest_id, edge_value],...]]
giraph = []
srcIndices = {}
counter = 0
for edge in edges:
    srcEdge = edge[0]
    destEdge = edge[1]
    if srcEdge not in srcIndices:
        giraph.append([srcEdge, [[destEdge, 1]]])
        srcIndices[srcEdge] = counter
        counter += 1

    else:
        indx = srcIndices[srcEdge]
        giraph[indx][1].append([destEdge, 1])

print(giraph)
