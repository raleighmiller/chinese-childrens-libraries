# import libraries
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

dianping = 'https://www.dianping.com/search/keyword/'
searchterm = '/0_%E7%BB%98%E6%9C%AC%E9%A6%86'

#loop to get first 10 results pages
for n in range(0,10):

    site = dianping + str(n) + searchterm
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)

    #open URL
    page = urlopen(req)
    soup = BeautifulSoup(page)
    print(soup)
