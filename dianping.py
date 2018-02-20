from bs4 import BeautifulSoup
import requests

r  = requests.get("http://www.dianping.com/citylist")
data = r.text

soup = BeautifulSoup(data, "html.parser")

city_list = {}

for link in soup.find_all("a", class_="link onecity"):
    city_list[link.get_text()] = 'http:' + link.get('href')

