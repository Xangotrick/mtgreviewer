import json
from class_Card import carddict,card

def getmodernC():
    f = open("topmodernC.txt")
    i = 0
    returner = set()
    for x in f:
        if (i % 2 == 0):
            returner.add(" ".join((x.split(" "))[1:]).replace("\t", "").rstrip())
        i += 1
    return returner


def getmodernS():
    f = open("topmodernS.txt")
    i = 0
    returner = set()
    for x in f:
        if (i % 2 == 0):
            returner.add(" ".join((x.split(" "))[1:]).replace("\t", "").rstrip())
        i += 1
    return returner


def writekeywords():
    f = open("../keywordlist.txt")
    r = open("../keyword", "w")
    for i in f:
        l = i.split(' ')
        r.write(l[-1])


def loadrandomkeywords():
    keylist = []
    f = open('../keyword')
    for i in f:
        keylist.append(i.lower())
    newlist = keylist.copy()
    random.shuffle(newlist)
    setofkeys = newlist[:10]
    print(setofkeys)
    return setofkeys


def loadcarddict():
    f = open('oracle-cards-20220630210230.json', encoding="utf-8")
    data = json.load(f)
    tempdict = dict()
    for i in data:
        if "//" not in i["name"]:
            tempdict[i["name"]] = card(i)
        else:
            if "card_faces" in i.keys():
                stri = i["card_faces"]
                for q in stri:
                    tempdict[q["name"]] = card(i, q)
    f.close()
    global acarddict
    return carddict(tempdict)
