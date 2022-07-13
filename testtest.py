strlist = []
r = open("testlist.txt")
for l in r:
    strlist.append(l.rstrip())
for l in strlist:
    print(l[-1])
    if l[-1] == ";":
        print(l)
        textlist = l.split(";")
        imgurl = textlist[1]
        break
imgurl = '"'+imgurl+'"'
