#!/usr/bin/env python

import json

def clean_label(label):
    return label.replace('http://www.cidoc-crm.org/cidoc-crm/', '').replace('http://www.ics.forth.gr/isl/CRMsci/', '').replace('http://www.ics.forth.gr/isl/CRMba/', '')

def main():
    with open('scripts/converted_gml.json') as f:
        data = json.load(f)

    with open('scripts/node_ids.json') as f:
        node_ids = json.load(f)

    node_ids = set(node_ids)
    cleaned_edges = []

    for edge in data['edges']:
        if (edge['source'] in node_ids) and (edge['target'] in node_ids):
            edge['title'] = clean_label(edge['label'])
            del edge['label']
            cleaned_edges.append(edge)

    json_edges = json.dumps(cleaned_edges)

    cleaned_nodes = []
    for node in data['nodes']:
        node['label'] = clean_label(node['label'])
        node['title'] = clean_label(node['label'])
        cleaned_nodes.append(node)

    json_nodes = json.dumps(cleaned_nodes)
    cleaned_result = '{"nodes":' + json_nodes + ',"links":' + json_edges + '}'
    print(cleaned_result)

if __name__ == '__main__':
    main()