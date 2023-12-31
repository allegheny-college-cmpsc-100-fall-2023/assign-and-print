#scrapes content from trinket.io web editor to main.py
#https://stackoverflow.com/questions/2081586/web-scraping-with-python
#https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont

import re
import requests
import json
import sys

#get url from README.md


file = open('LINK.md', 'r')
file = file.read()
#get all urls from file
url = re.search('trinket.io/.*', file).group(0)
#if url contains paren, remove it and all characters after it
if ')' in url:
    url = url[:url.index(')')]

#if url contains ], remove it and all characters after it
if ']' in url:
    url = url[:url.index(']')]

#if url format is https://trinket.io/library/trinkets/*, cnage it to https://trinket.io/python/*
if 'library/trinkets' in url:
    url = url.replace('library/trinkets', 'python')


#if last character in url is not alphanumeric, remove it
if not url[-1].isalnum():
    url = url[:-1]

#format url to embed link so python from editor can be scraped
#insert "embed/" between "trinket.io/" and "python /"
url = 'https://' + url[:11] + "embed/" + url[11:]
print(url)

#get the html from the url
html = requests.get(url).text

#get trinketObject.content from html 
trinketObject = re.search('trinketObject = (.*);', html).group(1)
trinketObject = json.loads(trinketObject)
python = trinketObject['code']

#write python from editor to file
f = open("main.py", "w")
f.write(str(python))
f.close()

