# Note: This script is just an illustration. It contains a very simple solution
# to the problem, which is far from perfect.

import urllib.request
import xml.etree.ElementTree as ET

URL = 'http://planetpython.org/rss20.xml'
with urllib.request.urlopen(URL) as url:
    doc = ET.parse(url)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(f'{title}\n{date}\n{link}\n')
