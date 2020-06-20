#!/usr/bin/env python

import json

def main():
    with open('full_topic_nodes.json') as f:
        data = json.load(f)

    with open('nodes.json') as f:
        node_ids = json.load(f)

    node_ids = set(node_ids)
    cleaned_edges = []
    
    for edge in data['edges']:
        if str(edge['source']) in node_ids or str(edge['target']) in node_ids:
            cleaned_edges.append(edge)

    print(json.dumps(cleaned_edges))


if __name__ == '__main__':
    main()