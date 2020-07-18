#!/usr/bin/env python
import json
import re

def main():
    with open('scripts/topic_nodes.json') as f:
        data = json.load(f)

    nodes = data['nodes']
    nodes_dict = {}
    for node in nodes:
        nodes_dict[node['id']] = node['label']
    print(json.dumps(nodes_dict))

if __name__ == '__main__':
    main()