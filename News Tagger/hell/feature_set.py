import os
import csv
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle

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
    for news in buis_news:                   #for Buisness
        f = open(news)
        r = f.read()
        words.extend(r.split(" "))
        print('buis',c)


    for news in sport_news:               #this will done when new dataset is found for sport 
        f1 = open(news)
        r = f1.read()
        words.extend(r.split(" "))


   
    for news in tech_news:                #for tech
        f2 = open(news)
        r = f2.read()
        words.extend(r.split(" "))



    for news in politics_news:            #for politics
        f3 = open(news)
        r = f3.read()
        words.extend(r.split(" "))


    for news in entertain_news:           #for entertain
        f4 = open(news)
        r = f4.read()
        words.extend(r.split(" "))

    

    for news in health_news:           #for health
        f4 = open(news)
        r = f4.read()
        words.extend(r.split(" "))

    
    for i in range(len(words)):           #checking if it is word or other in each file
        if not words[i].isalpha():
            words[i] = ""

    words = [x.lower() for x in words]

    dictionary = Counter(words)           # It counts the number of occurence of words
    del dictionary[""]
    dict1 = dictionary.most_common(3000)
    
    #adding dict to csv
    
    with open('Names.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for data in dict1:
            writer.writerow(data)
    return dict1

def feature_set(dict1):
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

    final_news = []
    feature_set = []
    labels = []

    final_news.extend(buis_news)
    final_news.extend(politics_news)
    final_news.extend(entertain_news)
    final_news.extend(sport_news)
    final_news.extend(tech_news)
    final_news.extend(health_news)

    c = len(final_news)
    
    for news in final_news:
        data = []
        f = open(news)
        words = f.read().split(" ")
        for entry in dict1:
            data.append(words.count(entry[0])) # jo common words hai words aur dict1[0] unko count karke data me append kiye so hai
        feature_set.append(data)
        
        if "politics" in news:
            labels.append("politics")
        if "sport" in news:
            labels.append("sports")
        if "buisness" in news:
            labels.append("buisness")
        if "tech" in news:
            labels.append("tech")
        if "entertainment" in news:
            labels.append("entertainment")
        if "health" in news:
            labels.append("health")
        
        print(c)
        c = c - 1
    return feature_set, labels

d = {}
reader = csv.reader(open('Names.csv','r'))
c = 38000
for row in reader:
    print(c)
    c = c - 1
    k,v = row
    d[k] = v

features, labels = feature_set(d)
print("Got Feature set")
print(len(features),len(labels))
print("Model is being trained")
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print(accuracy_score(y_test,preds))
print("File Opened")
with open('my-model','wb') as f:
    pickle.dump(clf, f)
print("File Saved and closed")
