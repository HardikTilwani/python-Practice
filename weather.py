import requests                                        #imported request module
from bs4 import BeautifulSoup                          #imported BeutifulSoup
search="weather in ahmedabad"                          
url=f"https://www.google.com/search?&q={search}"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
update=s.find("div",class_="BNeawe").text
print(update)
