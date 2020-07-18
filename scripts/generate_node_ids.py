#!/usr/bin/env python

import json
import sys

def main(jsonfile):
    with open(jsonfile) as f:
        data = json.load(f)

    node_ids = []
    for node in data['nodes']:
        node_ids.append(node['id'])
    print(node_ids)

if __name__ == '__main__':
    main(sys.argv[1])