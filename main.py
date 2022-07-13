from cgitb import text
from posixpath import split
import  sys
from tkinter.filedialog import test
from turtle import back
from flask import Flask, redirect,render_template, request, url_for
from forms import LoginForm
import requests
import json
from class_Card import card,carddict
from rfile import *
from set import *


def loadtxt(thetxt):
    answlist = []
    r = open(thetxt + ".txt")
    for l in r:
        answlist.append(l.rstrip())
    r.close()
    return answlist

def isstrinstr(thecard,thelist):
    for i in thelist:
        if thecard.lower() in i.lower():
            return True
    return False

def issetincards(carddict, asetcode):
    for ckey in carddict.dicte.keys():
        c = carddict.dicte[ckey]
        if c.set.lower() == asetcode.lower():
            return True
    return False

def rewrite(aname, anint,aperson):
    r = open(aperson+".txt",'a')
    txt = aname+ ";"+str(anint)+"\n"
    r.write(txt)
    r.close()

def get_json_data_set():
    response_API = requests.get('https://api.scryfall.com/sets')
    data = response_API.text
    return json.loads(data) 

def build_setlist(json_data_set,carddata):
    numsets = len(json_data_set['data'])
    listofsets =[]
    for i in range(numsets):
        setcode = json_data_set['data'][i]['code']
        if not 'token' in json_data_set['data'][i]['name'].lower():
            if not 'art series' in json_data_set['data'][i]['name'].lower():
                if not 'minigame' in json_data_set['data'][i]['name'].lower():
                    if issetincards(acarddict,setcode):
                        aset = set(json_data_set['data'][i],carddata)
                        listofsets.append(aset)
    return listofsets

#///INIT
acarddict = loadcarddict()
json_data_set = get_json_data_set()
listofsets = build_setlist(json_data_set,acarddict)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')




@app.route('/users/<name>')
def user(name):
    testedcards = loadtxt(name)
    if name in ['Kroux','Titi']:
        sumset = 0
        for i in listofsets:
            i.refreshperson(name,testedcards)
            sumset += len(i.clist)
            sumset += len(i.ulist)
            sumset += len(i.rlist)
            sumset += len(i.mlist)
        
        
        return render_template('sets.html',listofsets = listofsets,sumtot = sumset,sumreview = len(testedcards),percent =int(len(testedcards)/sumset*1000) / 10 )
    else:
        return redirect("/index", code=302)





@app.route('/users/<name>/<set>',methods=['GET','POST'])
def userset(name,set):
    tempsetlist = []
    for key in acarddict.dicte.keys():
        acard = acarddict.dicte[key]
        if acard.set.lower() == set.lower():
            tempsetlist.append(acard)
    tempsetlist = sorted(tempsetlist, key = lambda ex : int(ex.cmc))
    setlist = []
    for r in ['bonus','mythic','rare','uncommon','common']:
        for c in tempsetlist:
            if c.rarity == r:
                setlist.append(c)

    testedcards = loadtxt(name)
    imgurl = ''
    cardname = ''
    carde = None

    for c in setlist:
        if not isstrinstr(c.name,testedcards):
            imgurl = c.imguri["large"]
            cardname = c.name
            carde = c
            print(c.name)
            break

    backurl = "/users/"+name
    
    form = LoginForm()
    if form.validate_on_submit():
        print("hey")
        rewrite(cardname,request.form["building"],name)
        return redirect('/users/'+name+'/'+set)

    return render_template('carddisplay.html',form = form,theurl = imgurl, carde = carde, backurl = backurl)