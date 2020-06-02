class Marksheet:
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
        # just showing all data in terminal
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
        
    def calculateTotal(self,mark):
        # create sum of cq, mcq and practical
        marks = mark.split("+")
        total = 0
        for i in marks:
            total += int(i)
        return total
        
    def setTotal(self):
        # total marks added
        self.bantotal = self.calculateTotal(self.ban1) + self.calculateTotal(self.ban2)
        self.engtotal = self.calculateTotal(self.eng1) + self.calculateTotal(self.eng2)
        self.icttotal = self.calculateTotal(self.ict)
        self.phytotal = self.calculateTotal(self.phy1) + self.calculateTotal(self.phy2)
        self.chetotal = self.calculateTotal(self.che1) + self.calculateTotal(self.che2)
        self.mathtotal = self.calculateTotal(self.math1) + self.calculateTotal(self.math2)
        self.biototal = self.calculateTotal(self.bio1) + self.calculateTotal(self.bio2)
        
    def checkTotal(self):
        # just for checking total marks
        print(f"total in bangla : {self.bantotal}")
        print(f"total in englilsh : {self.engtotal}")
        print(f"total in ict : {self.icttotal}")
        print(f"total in phy : {self.phytotal}")
        print(f"total in che : {self.chetotal}")
        print(f"total in math : {self.mathtotal}")
        print(f"total in bio : {self.biototal}")