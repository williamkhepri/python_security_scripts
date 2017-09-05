import urllib2
response = urllib2.urlopen('http://www.google.com/')
print response.info()
html = response.read()
response.close()

