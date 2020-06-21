#!/usr/bin/env python

import json

def clean_label(label):
    return label.replace('http://www.cidoc-crm.org/cidoc-crm/', '').replace('http://www.ics.forth.gr/isl/CRMsci/', '').replace('http://www.ics.forth.gr/isl/CRMba/', '')

def main():
    with open('full_topic_nodes.json') as f:
        data = json.load(f)

    with open('nodes.json') as f:
        node_ids = json.load(f)

    node_ids = set(node_ids)
    cleaned_edges = []
    
    for edge in data['edges']:
        if (str(edge['source']) in node_ids) and (str(edge['target']) in node_ids):
            edge['title'] = clean_label(edge['label'])
            del edge['label']
            cleaned_edges.append(edge)

    # print(json.dumps(cleaned_edges))
    # print(len(cleaned_edges))
    cleaned_nodes = []
    for node in data['nodes']:
        node['label'] = clean_label(node['label'])
        node['title'] = clean_label(node['label'])
        cleaned_nodes.append(node)

    print(json.dumps(cleaned_nodes))

if __name__ == '__main__':
    main()