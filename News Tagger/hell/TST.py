import os
import csv
from collections import Counter


def preProcessing():
    words = []
    buis_direc = "dataset\\buisness\\"
    sport_direc = "dataset\\sport\\"
    tech_direc = "dataset\\tech\\"
    politics_direc = "dataset\\politics\\"
    entertain_direc = "dataset\\entertainment\\"
    health_direc = "dataset\\health\\"
    
    files1 = os.listdir(buis_direc)
    files2 = os.listdir(sport_direc)
    files3 = os.listdir(tech_direc)
    files4 = os.listdir(politics_direc)
    files5 = os.listdir(entertain_direc)
    files6 = os.listdir(health_direc)
    
    buis_news = [buis_direc + buis_news for buis_news in files1]
    sport_news = [sport_direc + sport_news for sport_news in files2]
    tech_news = [tech_direc + tech_news for tech_news in files3]
    politics_news = [politics_direc + politics_news for politics_news in files4]
    entertain_news = [entertain_direc + entertain_news for entertain_news in files5]
    health_news = [health_direc + health_news for health_news in files6]

    print("PrePRo started")
    c = len(buis_news)
    for news in buis_news:                   #for Buisness
        f = open(news)
        r = f.read()
        words.extend(r.split(" "))
        print('buis',c)
        c-=1
    print("Buisness done")
    
    c = len(sport_news)
    for news in sport_news:               #this will done when new dataset is found for sport 
        f1 = open(news)
        r = f1.read()
        words.extend(r.split(" "))
        print('sport',c)
        c-=1
    print("sports done")
    
    
    c = len(tech_news)
    for news in tech_news:                #for tech
        f2 = open(news)
        r = f2.read()
        words.extend(r.split(" "))
        print('tech',c)
        c-=1
    print("tech done")
    
    c = len(politics_news)
    for news in politics_news:            #for politics
        f3 = open(news)
        r = f3.read()
        words.extend(r.split(" "))
        print('politics',c)
        c-=1
    print("politics done")
    
    c = len(entertain_news)
    for news in entertain_news:           #for entertain
        f4 = open(news)
        r = f4.read()
        words.extend(r.split(" "))
        print('entertain',c)
        c-=1
    print("e done")
    
    c = len(health_news)
    for news in health_news:           #for health
        f4 = open(news)
        r = f4.read()
        words.extend(r.split(" "))
        print('health',c)
        c-=1
    print("health done")
    
    for i in range(len(words)):           #checking if it is word or other in each file
        if not words[i].isalpha():
            words[i] = ""
    words = [x.lower() for x in words]

    # dictionary = {}
    # dictionary = Counter(words)           # It counts the number of occurence of words
    # del dictionary[""]
    # dict1 = dictionary.most_common(100000)

    # #adding dict to csv
    
    with open('words.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for data in words:
            writer.writerow([data])
            
preProcessing()

# reader = csv.reader(open('words.csv','r'))
# my = []
# for row in reader:
#     my.extend(row)
# print(my)
# #     #c = c - 1
# # result = ''
# # for ele in words:
# #     for entry in ele:
# #         result += str(entry)
# #     my.append(result)

# # print(my)
