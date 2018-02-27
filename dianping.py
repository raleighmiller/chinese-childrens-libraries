from bs4 import BeautifulSoup
import requests

r  = requests.get("http://www.dianping.com/citylist")
data = r.text

soup = BeautifulSoup(data, "html.parser")

city_list = {}

for link in soup.find_all("a", class_="link onecity"):
    city_list[link.get_text()] = 'http:' + link.get('href')

'''    
    This prints a list of ('chinese city name' : 'http://www.dianping.com/chinesecityname')
In the header of each city url the CityId, cityCName, cityEName are listed
Next step is probably going to be setting up a for loop and parsing each url for these
three values and putting them in an array.  We tried doing this but are unsure how efficient
it is to scrape 200 pages individually, did not get anywhere with it.
'''
