import urllib
from bs4 import BeautifullSoup
url = "http://www.subtorrents.com/peliculas/estrenos/"
page = urllib.openurl(url)
source = BeautifullSoup(page, "html.parser")
print source.find("title").text
