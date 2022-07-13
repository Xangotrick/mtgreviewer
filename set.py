class set:
    def __init__(self,jsonitem,carddata):
        self.name = jsonitem['name']
        self.code = jsonitem['code']
        self.uri = jsonitem['icon_svg_uri']
        self.weburl = '/users/'+"/" + self.code

        self.clist = []
        self.ulist = []
        self.rlist = []
        self.mlist = []

        for i in carddata.dicte.keys():
            c = carddata.dicte[i]
            if self.code == c.set:
                if c.rarity == "common":
                    self.clist.append(c)
                if c.rarity == "uncommon":
                    self.ulist.append(c)
                if c.rarity == "rare":
                    self.rlist.append(c)
                if c.rarity == "mythic":
                    self.mlist.append(c)

        self.userc = []
        self.useru = []
        self.userr = []
        self.userm = []


    def refreshperson(self, aname,stringlist):
        self.weburl = '/users/'+aname+"/" + self.code
        self.userc = []
        self.useru = []
        self.userr = []
        self.userm = []
        for s in stringlist:
            for c in self.clist:
                if c.name in s:
                    self.userc.append(c.name)
            for c in self.ulist:
                if c.name in s:
                    print(c.name)
                    self.useru.append(c.name)
            for c in self.rlist:
                if c.name in s:
                    self.userr.append(c.name)
            for c in self.mlist:
                if c.name in s:
                    self.userm.append(c.name)

    def faggot(self):
        returner = ""
        returner +=  "M: "+str(len(self.userm)) +"/" +str(len(self.mlist))+", "
        returner +=  "R: "+str(len(self.userr)) +"/" +str(len(self.rlist))+", "
        returner +=  "U: "+str(len(self.useru)) +"/" +str(len(self.ulist))+", "
        returner +=  "C: "+str(len(self.userc)) +"/" +str(len(self.clist))
        return returner

    def checkfill(self):
        return (len(self.userm) < len(self.mlist)) or (len(self.userr) < len(self.rlist)) or (len(self.useru) < len(self.ulist)) or (len(self.userc) < len(self.clist))