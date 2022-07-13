from cgitb import text
from posixpath import split
import  sys
from flask import Flask,render_template, request
from forms import LoginForm


strlist = []
answlist = []
r = open("testlist.txt")
for l in r:
    strlist.append(l.rstrip().split(";"))
r.close()
r = open("answers.txt")
for l in r:
    answlist.append(l.rstrip())
r.close()

spellname=  ""
imgurl = ""
for l in strlist:
    abool = True
    for i in answlist:
        if l[0] in i:
            abool = False
            break
    if abool:
        imgurl = l[1]
        spellname = l[0]
        break
def loadtxt():
    strlist = []
    answlist = []
    r = open("testlist.txt")
    for l in r:
        strlist.append(l.rstrip().split(";"))
    r.close()
    r = open("answers.txt")
    for l in r:
        answlist.append(l.rstrip())
    r.close()
    global spellname
    global imgurl
    spellname=  ""
    imgurl = ""
    for l in strlist:
        abool = True
        for i in answlist:
            if l[0] in i:
                abool = False
                break
        if abool:
            imgurl = l[1]
            spellname = l[0]
            break

def rewrite(aname, anint):
    for i in strlist:
        if i[0] == aname:
            strlist[2] = str(anint)

    r = open("answers.txt",'a')
    txt = aname+ ";"+str(anint)+"\n"
    r.write(txt)
    r.close()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/',methods=['GET','POST'])
def index():
    loadtxt()
    form = LoginForm()
    if form.validate_on_submit():
        rewrite(spellname,request.form["building"])
    return render_template('index.html',form = form,theurl = imgurl)

@app.route('/users/<name>')
def user(name):
    theame = name +" is gay"
    return render_template('carddisplay.html', thename = theame)


