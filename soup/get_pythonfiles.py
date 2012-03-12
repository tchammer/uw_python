"""
Demonstrate screen scraping with BeautifulSoup 

Installed from http://www.crummy.com/software/BeautifulSoup/#Download/ 
Explained at http://www.crummy.com/software/BeautifulSoup/documentation.html
"""

import urllib2
import re
from pprint import pprint
from BeautifulSoup import BeautifulSoup

# read a web page into a big string
baseurl = 'http://jon-jacky.github.com/uw_python/winter_2012/'
page = urllib2.urlopen('http://jon-jacky.github.com/uw_python/winter_2012/index.html').read()

# parse the string into a "soup" data structure
soup = BeautifulSoup(page)

# find all the anchor tags that link to Python files
pythonfiles = soup.findAll('a',attrs={'href':(lambda a: a and a.endswith('.py'))})

for link in pythonfiles:
    url = baseurl + link.attrs[0][1]
    page = urllib2.urlopen(url).read()
    
    filename = (link.attrs[0][1].split('/'))[-1]

    fh = open(filename, "w+")
    fh.write(page)
    fh.close()

