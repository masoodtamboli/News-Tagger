import os
import csv
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle

def feature_set():
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

    # final_news.extend(buis_news)
    # final_news.extend(politics_news)
    # final_news.extend(entertain_news)
    final_news.extend(sport_news)
    # final_news.extend(tech_news)
    # final_news.extend(health_news)

    c = len(final_news)
    
    for news in final_news:
        data = []
        f = open(news)
        words = f.read().split(" ")
        # for entry in dict1:
        #     data.append(words.count(entry[0])) # jo common words hai words aur dict1[0] unko count karke data me append kiye so hai
        # feature_set.append(data)
        
        # if "politics" in news:
        #     labels.append("politics")
        # if "sport" in news:
        #     labels.append("sports")
        # if "buisness" in news:
        #     labels.append("buisness")
        # if "tech" in news:
        #     labels.append("tech")
        # if "entertainment" in news:
        #     labels.append("entertainment")
        # if "health" in news:
        #     labels.append("health")
        
        # print(c)
        # c = c - 1
        with open('words.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            for data in words:
                writer.writerow([data])

feature_set()

