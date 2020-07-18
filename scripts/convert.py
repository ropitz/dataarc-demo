#!/usr/bin/env python
import sys
import re

def node_ids(nodes):
    regex = re.compile('"id":([0-9]+)')
    node_ids = regex.findall(nodes)
    return node_ids

def gml_sub(blob):
    lines = []
    for line in blob.split('\n'):
        line = line.strip()
        lines.append(line)
    blob = "\n".join(lines)

    blob = blob.replace('\n\n', '\n')
    blob = blob.replace(']\n', '},\n')
    blob = blob.replace('[\n', '{')
    blob = blob.replace('\n{', '\n    {')
    
    blob = blob.replace('id ', '"id":')

    for s in ['label', 'source', 'target', 'value']:
        blob = blob.replace(s, '"%s":' % s)
    blob = blob.replace('\n"', ', "')
    blob = blob.replace('\n}', '}')
    return blob.strip('\n')

def main(graphfile):
    with open(graphfile, 'r') as f:
        blob = f.read()
    blob = ''.join(blob.split('node')[1:])
    nodes = re.split(r'\bedge\b', blob, 1)[0]
    edges = re.split(r'\bedge\b', blob, 1)[1]

    nodes = gml_sub(nodes)
    edges = gml_sub(edges)
    edges = edges.replace('edge ', '')
    print('{\n  "nodes":[')
    print(nodes.rstrip(','))
    print('  ],\n  "edges":[')
    print('    ' + edges.rstrip(','))
    print('  ]\n}\n')

if __name__ == '__main__':
    main(sys.argv[1])