class Marksheet:
    # total marks
    bantotal = 0
    engtotal = 0
    icttotal = 0
    phytotal = 0
    chetotal = 0
    mathtotal = 0
    biototal = 0
    
    # gpa points
    bangpa = 0.0
    enggpa = 0.0
    ictgpa = 0.0
    phygpa = 0.0
    chegpa = 0.0
    mathgpa = 0.0
    biogpa = 0.0
    
    # grade marks
    bangrade = ""
    enggrade = ""
    ictgrade = ""
    phygrade = ""
    chegrade = ""
    mathgrade = ""
    biograde = ""
    
    # result
    resultgpa = 0.0
    resultgrade = ""
    
    def __init__(self, info):
        self.roll = str(info[0])
        self.name = info[1]
        self.co = info[2]
        self.phone = info[3]
        self.session = info[4]
        self.collage = info[5]
        self.fourthsub = info[6]
        self.ban1 = info[7]
        self.ban2 = info[8]
        self.eng1 = info[9]
        self.eng2 = info[10]
        self.ict = info[11]
        self.phy1 = info[12]
        self.phy2 = info[13]
        self.che1 = info[14]
        self.che2 = info[15]
        self.math1 = info[16]
        self.math2 = info[17]
        self.bio1 = info[18]
        self.bio2 = info[19]
        
    def show(self):
        print(self.roll)
        print(self.name)
        print(self.co)
        print(self.phone)
        print(self.session)
        print(self.collage)
        print(self.fourthsub)
        print(self.ban1)
        print(self.ban2)
        print(self.eng1)
        print(self.eng2)
        print(self.ict)
        print(self.phy1)
        print(self.phy2)
        print(self.che1)
        print(self.che2)
        print(self.math1)
        print(self.math2)
        print(self.bio1)
        print(self.bio2)