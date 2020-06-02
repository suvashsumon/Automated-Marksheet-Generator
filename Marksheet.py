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
    
    def calGpa(self,mark):
        # calculate gpa
        m = mark/2
        if m>=80:
            return "5.00"
        elif m<80 and m>=70:
            return "4.00"
        elif m<70 and m>=60:
            return "3.50"
        elif m<60 and m>=50:
            return "3.00"
        elif m<50 and m>=40:
            return "2.50"
        elif m<40 and m>=33:
            return "2.00"
        else:
            return "0.00"
        
    def setGpa(self):
        # setting gpa
        self.bangpa = self.calGpa(self.bantotal)
        self.enggpa = self.calGpa(self.engtotal)
        self.ictgpa = self.calGpa(self.icttotal*2)
        self.phygpa = self.calGpa(self.phytotal)
        self.chegpa = self.calGpa(self.chetotal)
        self.mathgpa = self.calGpa(self.mathtotal)
        self.biogpa = self.calGpa(self.biototal)
        
    def checkGpa(self):
        # just for checking gpa
        print(f"gpa in bangla : {self.bangpa}")
        print(f"gpa in englilsh : {self.enggpa}")
        print(f"gpa in ict : {self.ictgpa}")
        print(f"gpa in phy : {self.phygpa}")
        print(f"gpa in che : {self.chegpa}")
        print(f"gpa in math : {self.mathgpa}")
        print(f"gpa in bio : {self.biogpa}")
        
    def calGrade(self,mark):
        # cal grade
        m = mark / 2
        if m>=80:
            return "A+"
        elif m<80 and m>=70:
            return "A"
        elif m<70 and m>=60:
            return "A-"
        elif m<60 and m>=50:
            return "B"
        elif m<50 and m>=40:
            return "C"
        elif m<40 and m>=33:
            return "D"
        else:
            return "F"
        
    def setGrade(self):
        # setting grade
        self.bangrade = self.calGrade(self.bantotal)
        self.enggrade = self.calGrade(self.engtotal)
        self.ictgrade = self.calGrade(self.icttotal*2)
        self.phygrade = self.calGrade(self.phytotal)
        self.chegrade = self.calGrade(self.chetotal)
        self.mathgrade = self.calGrade(self.mathtotal)
        self.biograde = self.calGrade(self.biototal)
        
    def checkGrade(self):
        # just for checking grade
        print(f"grade in bangla : {self.bangrade}")
        print(f"grade in englilsh : {self.enggrade}")
        print(f"grade in ict : {self.ictgrade}")
        print(f"grade in phy : {self.phygrade}")
        print(f"grade in che : {self.chegrade}")
        print(f"grade in math : {self.mathgrade}")
        print(f"grade in bio : {self.biograde}")