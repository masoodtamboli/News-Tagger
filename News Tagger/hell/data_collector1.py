import requests
import re
from bs4 import BeautifulSoup
import random

def get1():
    URLs = ["https://en.wikipedia.org/wiki/Sport" , "https://en.wikipedia.org/wiki/Sport_in_India", ""]
    r = requests.get(URL2)
    soup = BeautifulSoup(r.content,'html.parser')
    var = []
    news = []
    for i in range(70):
        temp = soup.find('div', {'class' : 'mw-parser-output'}).find_all('p')[i].text
        news.append(temp)
        var = "news/sport/sport"+str(random.randrange(0,1000,1))+".txt"
        f = open(var,'w')
        f.write(news[i])
        f.close()
        print(news)

get1()