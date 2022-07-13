import ast

class card:


    def __init__(self,adict, cardface = None):
        thedict = adict

        if cardface == None:
            self.name = thedict["name"]
            self.mana = thedict["mana_cost"]
            self.typetxt = thedict["type_line"]
            self.text = thedict["oracle_text"]
            res = ast.literal_eval(str(thedict["image_uris"]))
            self.imguri = res
            self.set = thedict["set"]
            self.rarity = thedict["rarity"]
            if "power" in thedict.keys():
                self.power = thedict["power"]
            if "toughness" in thedict.keys():
                self.toughness = thedict["toughness"]
            self.colorid = thedict["color_identity"]
            self.color = thedict["colors"]
            self.cmc = thedict['cmc']
            self.prices = thedict['prices']
            for key in self.prices:
                if self.prices[key] == None:
                    self.prices[key] = 0
        else:
            self.name = cardface["name"]
            self.mana = cardface["mana_cost"]
            if "type_line" in adict.keys():
                self.typetxt = adict["type_line"]
            else:
                self.typetxt = cardface["type_line"]
            self.text = cardface["oracle_text"]
            if "image_uris" in adict.keys():
                res = ast.literal_eval(str(adict["image_uris"]))
            else:
                res = ast.literal_eval(str(cardface["image_uris"]))
            self.imguri = res
            self.set = adict["set"]
            self.rarity = adict["rarity"]
            self.cmc = adict['cmc']
            self.prices = adict['prices']
            for key in self.prices:
                if self.prices[key] == None:
                    self.prices[key] = 0
            if "power" in cardface.keys():
                self.power = cardface["power"]
            if "toughness" in cardface.keys():
                self.toughness = cardface["toughness"]

            if "color_identity" in adict.keys():
                self.colorid = adict["color_identity"]
            else:
                self.colorid = cardface["color_identity"]

            if "colors" in adict.keys():
                self.color = adict["colors"]
            else:
                self.color = cardface["colors"]
        self.estimation = 0

    def print(self):
        print("///////////////////")
        print('')
        print(self.name +"  " +self.mana)
        print("")
        print(self.typetxt + "   " + self.set + " " + self.rarity)
        print("")
        print(self.text)
        if "creature" in self.typetxt.lower():
            print("")
            print(self.power+"/"+self.toughness)
        print('')
        print("///////////////////")
    @staticmethod
    def isreprint(card1,card2):
        if card1.set != card2.set:
            if card1.mana == card2.mana:
                if card1.typetxt == card2.typetxt:
                    TAX1 = card1.text.replace(card1.name,"")
                    TAX2 = card2.text.replace(card2.name,"")
                    if TAX1 == TAX2:
                            return True
        return False






class carddict:
    def __init__(self, adict):
        self.dicte = adict
        self.dictw = []
        self.dictu = []
        self.dictb = []
        self.dictr = []
        self.dictg = []
        self.dictc = []
        self.dictm = []
        self.landdict = dict()

        for val in self.dicte.values():
            val : card
            if len(val.color) == 0:
                self.dictc.append(val)
            elif len(val.color) >= 2:
                self.dictm.append(val)
            else:
                C = val.color[0]
                if C == 'W':
                    self.dictw.append(val)
                if C == 'U':
                    self.dictu.append(val)
                if C == 'B':
                    self.dictb.append(val)
                if C == 'R':
                    self.dictr.append(val)
                if C == 'G':
                    self.dictg.append(val)

    def buildlands(self):
        biglist = []
        # origin:
        biglist.append(['origin', 20, 'Tundra', 'Underground Sea', 'Badlands', 'Taiga', 'Savannah', 'Scrubland', 'Volcanic Island','Bayou', 'Plateau', 'Tropical Island'])
        biglist.append(['pain', 17.5, 'Adarkar Wastes', 'Underground River', 'Sulfurous Springs', 'Karplusan Forest', 'Brushland','Caves of Koilos', 'Shivan Reef', 'Llanowar Wastes', 'Battlefield Forge', 'Yavimaya Coast'])
        biglist.append(['horizon', 13.5, 'Silent Clearing', 'Fiery Islet', 'Nurturing Peatland', 'Sunbaked Canyon','Waterlogged Grove'])
        biglist.append(["painother", 17, 'Ancient Tomb', 'City of Brass'])
        biglist.append(['fetchbad', 10, 'Flood Plain', 'Bad River', 'Rocky Tar Pit', 'Mountain Valley', 'Grasslands'])
        biglist.append(["fetch", 19, 'Flooded Strand', 'Polluted Delta', 'Bloodstained Mire', 'Wooded Foothills','Windswept Heath', 'Marsh Flats', 'Scalding Tarn', 'Verdant Catacombs', 'Arid Mesa','Misty Rainforest'])
        biglist.append(['lifecapenna', 1, 'Brokers Hideout', 'Obscura Storefront', 'Maestros Theater', 'Riveteers Overlook','Cabaretti Courtyard'])
        biglist.append(['filterone', 10.5, 'Skycloud Expanse', 'Darkwater Catacombs', 'Shadowblood Ridge', 'Mossfire Valley','Sungrass Prairie'])
        biglist.append(['filtertwo', 14, 'Mystic Gate', 'Sunken Ruins', 'Graven Cairns', 'Fire-Lit Thicket', 'Wooded Bastion','Fetid Heath', 'Cascade Bluffs', 'Twilight Mire', 'Rugged Prairie', 'Flooded Grove'])
        biglist.append(['bounce', 11, 'Azorius Chancery', 'Dimir Aqueduct', 'Rakdos Carnarium', 'Gruul Turf', 'Selesnya Sanctuary','Orzhov Basilica', 'Izzet Boilerworks', 'Golgari Rot Farm', 'Boros Garrison', 'Simic Growth Chamber'])
        biglist.append(['shock', 18, 'Hallowed Fountain', 'Watery Grave', 'Blood Crypt', 'Stomping Ground', 'Temple Garden','Godless Shrine', 'Overgrown Tomb', 'Breeding Pool', 'Steam Vents', 'Sacred Foundry'])
        biglist.append(['scry', 15.5, 'Temple of Enlightenment', 'Temple of Deceit', 'Temple of Malice', 'Temple of Abandon','Temple of Plenty', 'Temple of Silence', 'Temple of Epiphany', 'Temple of Malady', 'Temple of Triumph','Temple of Mystery'])
        biglist.append(["battle", 13, 'Prairie Stream', 'Sunken Hollow', 'Smoldering Marsh', 'Cinder Glade', 'Canopy Vista'])
        biglist.append(['checkland', 15, 'Glacial Fortress', 'Drowned Catacomb', 'Dragonskull Summit', 'Rootbound Crag','Sunpetal Grove', 'Isolated Chapel', 'Sulfur Falls', 'Woodland Cemetery', 'Clifftop Retreat','Hinterland Harbor'])
        biglist.append(['fast', 16, 'Seachrome Coast', 'Darkslick Shores', 'Blackcleave Cliffs', 'Copperline Gorge','Razorverge Thicket', 'Concealed Courtyard', 'Spirebluff Canal', 'Blooming Marsh','Inspiring Vantage', 'Botanical Sanctum'])
        biglist.append(['reveal', 12, 'Port Town', 'Choked Estuary', 'Foreboding Ruins', 'Game Trail', 'Fortified Village','Shineshadow Snarl', 'Frostboil Snarl', 'Necroblossom Snarl', 'Furycalm Snarl', 'Vineglimmer Snarl'])
        biglist.append(['bicycle', 11, 'Irrigated Farmland', 'Fetid Pools', 'Canyon Slough', 'Sheltered Thicket','Scattered Groves', 'Indatha Triome', 'Raugrin Triome', 'Zagoth Triome', 'Savai Triome','Ketria Triome', "Jetmir's Garden", "Ziatora's Proving Ground", "Xander's Lounge","Raffine's Tower", "Spara's Headquarters"])
        biglist.append(['slowlife', 9, 'Tranquil Cove', 'Dismal Backwater', 'Bloodfell Caves', 'Rugged Highlands','Blossoming Sands', 'Scoured Barrens', 'Swiftwater Cliffs', 'Jungle Hollow','Wind-Scarred Crag', 'Thornwood Falls'])
        cardlist = []
        for landlist in biglist:
            speed = landlist[1]
            for j in range(2,len(landlist)):
                self.dicte[landlist[j]].estimation = speed
                thestr = ''
                for sr in self.dicte[landlist[j]].colorid:
                    thestr+= sr
                if thestr not in self.landdict.keys():
                    self.landdict[thestr] = []
                self.landdict[thestr].append(self.dicte[landlist[j]])




    def get(self,txt):
        for i in self.dicte.keys():
            if txt.lower() == i.lower():
                return self.dicte[i]
        for i in self.dicte.keys():
            if txt.lower() in i.lower():
                return self.dicte[i]
        return self.dicte["Urza, Academy Headmaster"]

    def filterAND(self, alist = [], color = '',type = '', CMC = None, rarity = '', text =''):
        workinglist = self.dicte.values()
        returnlist = []
        if color.lower() == 'w':
            workinglist = self.dictw
        if color.lower() == 'u':
            workinglist = self.dictu
        if color.lower() == 'b':
            workinglist = self.dictb
        if color.lower() == 'r':
            workinglist = self.dictr
        if color.lower() == 'g':
            workinglist = self.dictg
        if color.lower() == 'm':
            workinglist = self.dictm
        if color.lower() == 'c':
            workinglist = self.dictc

        if alist != []:
            workinglist = alist

        for i in workinglist:
            if type.lower() in i.typetxt.lower() and (CMC == int(i.cmc) or CMC == None) and rarity in i.rarity and text.lower() in i.text.lower():
                returnlist.append(i)
        return returnlist