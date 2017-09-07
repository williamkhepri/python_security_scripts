#!/usr/bin/python
import requests
import re

#get url
url = input('Introduce la URL: ("http://www.website.com"): ')

#connect to the url
website = requests.get(url)

#read html
html = website.text

#use re.findall to grab all the links
links =  re.findall('"((http|ftp)s?://.*?)"', html)

#output links
for link in links:
	print(link[0])

