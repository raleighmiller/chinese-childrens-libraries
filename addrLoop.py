#This file loops over all city codes set by n range and extracts address data from each entry

from bs4 import BeautifulSoup
import requests
import csv

addr_list = []

#loop over different cities
for n in range(1,10):
    base_url = "https://www.dianping.com/search/keyword/"+str(n)+"/0_%E7%BB%98%E6%9C%AC%E9%A6%86/"
    if n<4:
        for page in range(1, 13):
            print ("Code: " + str(n) + " Current page: " + str(page))

            url = base_url + 'p' + str(page)

            response = requests.get(url)
            data = response.text
            soup = BeautifulSoup(data, "html.parser")
            addr_list += soup.find_all('span',{'class':'addr'})
            
    else:
        for page in range(1, 5):
            print ("Code: " + str(n) + " Current page: " + str(page))

            url = base_url + 'p' + str(page)

            response = requests.get(url)
            data = response.text
            soup = BeautifulSoup(data, "html.parser")
            addr_list += soup.find_all('span',{'class':'addr'})
            
print(addr_list)
