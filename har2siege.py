#!/bin/python3

import sys
import json
import logging
import re

logging.basicConfig(format='%(levelname)s: %(message)s')

har = ''
har_filter = ''
data = {}

try:
    har = sys.argv[1]
except IndexError:
    logging.error('no HAR file in cli arg')
    exit(1)
try:
    har_filter = sys.argv[2]
except IndexError:
    pass
try:
    file = open(har)
except IOError as e:
    logging.error('%s: %s' % (e.strerror, e.filename))
    exit(1)
try:
    data = json.load(file)
    file.close()
    for key in data['log']['entries']:
        if re.search(har_filter, key['request']['url']):
            if key['request']['method'] == 'POST':
                if key['request']['bodySize'] != 0:
                    print(type(key['request']['postData']))
                    print(key['request']['url'], key['request']['method'], key['request']['postData']['text'])
            elif key['request']['method'] == 'GET':
                print(key['request']['url'])
except json.JSONDecodeError as e:
    logging.error('JSON parsing. %s' % e)
    exit(1)
