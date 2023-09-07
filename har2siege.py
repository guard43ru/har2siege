#!/bin/python3
# Usage: ./har2siege.py file.har > output.txt

import sys
import json

try:
    arg = sys.argv[1]
    file = open(arg)
    data = json.load(file)
    file.close()
except:
    print('Error: no HAR file')
try:
    for key in data['log']['entries']:
        print(key['request']['method'], key['request']['url'])
except:
    print('Error: parsing problem')


