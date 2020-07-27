import csv

def buisness():
    data = []
    words = []
    list1 = []

    with open ("dataset\\CSV\\buisness.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "buisness"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\buisness\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

def entertainment():
    data = []
    words = []
    list1 = []

    with open ("ataset copy\\CSV\\entertainment.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)
    print("Data is being retrieved...")

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "entertain"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\entertainment\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

def tech():
    data = []
    words = []
    list1 = []

    with open ("dataset\\CSV\\tech.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)
    print("Data is being retrieved...")

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "tech"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\tech\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

def health():
    data = []
    words = []
    list1 = []

    with open ("dataset\\CSV\\health.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)
    print("Data is being retrieved...")

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "health"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\health\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

def sports():
    data = []
    words = []
    list1 = []

    with open ("dataset\\CSV\\sport.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)
    print("Data is being retrieved...")

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "sport"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\sport\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

def politics():
    data = []
    words = []
    list1 = []

    with open ("dataset\\CSV\\politics.csv") as f:
        data.extend(csv.reader(f))

    c = len(data)
    print("Data is being retrieved...")

    for i in data:
        for j in i:
            words.append(j)
        
    for i in range(1001,200000):
        name = "politics"+str(i)+".txt"
        list1.append(name)

    for i in range(len(words)):
        var = "dataset\\politics\\"+list1[i]
        f = open(var,'w+')
        f.write(words[i])
        f.close()
        print(c)
        c = c - 1

#buisness()
#tech()
#health()
#sports()
politics()




