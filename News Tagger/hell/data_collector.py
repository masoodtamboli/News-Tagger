import requests
import re
from bs4 import BeautifulSoup
import random
import csv

def politics():
    URL = "https://economictimes.indiatimes.com/news/politics-nation?from=mdr"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')
    
    var = []
    news = []
    
    for i in range(10):
        temp = soup.find_all("div", {"class": "botplData flt"})[i].find("p").text
        news.append(temp)
        with open('words.csv','w') as f:
            wr = csv.writer(f)
            wr.writerow(news)
        # var = "news/politics/politics"+str(random.randrange(0,1000,1))+".txt"
        # f = open(var,'w')
        # f.write(news[i])
        # f.close()

#politics()