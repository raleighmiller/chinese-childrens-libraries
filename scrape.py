# small test to open a page at Dianpint
#import libraries
#this works for Raleigh
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#Getting around thinking we're a robot
site = 'http://dianping.com'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)

#open URL
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)
