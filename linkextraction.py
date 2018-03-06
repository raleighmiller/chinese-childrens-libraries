from bs4 import BeautifulSoup
import requests

r  = requests.get("http://www.dianping.com/citylist")
data = r.text

soup = BeautifulSoup(data, "html.parser")

link_list = {}

link_list = ['http:'+link['href'] for link in soup.find_all('a', class_= "link onecity", href=True)]

print(link_list)
