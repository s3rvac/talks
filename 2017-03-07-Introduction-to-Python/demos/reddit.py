# Note: This script is just an illustration. It contains a very simple solution
# to the problem, which is far from perfect.

import json
import urllib.request

URL = 'https://www.reddit.com/r/Python/.json'
with urllib.request.urlopen(URL) as url:
    text = url.read()

text = json.loads(text)
for data in text['data']['children']:
    data = data['data']
    print('{:<4} {:<15} {}'.format(
        data['score'],
        data['author'],
        data['title']
    ))
