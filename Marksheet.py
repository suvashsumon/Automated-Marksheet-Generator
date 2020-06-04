class Marksheet:
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
            return 5.00
        elif m<80 and m>=70:
            return 4.00
        elif m<70 and m>=60:
            return 3.50
        elif m<60 and m>=50:
            return 3.00
        elif m<50 and m>=40:
            return 2.50
        elif m<40 and m>=33:
            return 2.00
        else:
            return 0.00
        
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
        
    def calResultGpa(self):
        # calculate result in gpa
        res = self.bangpa + self.enggpa + self.ictgpa + self.phygpa + self.chegpa
        if self.fourthsub=="126":
            if self.bangrade!="F" and self.enggrade!="F" and self.ictgrade!="F" and self.phygrade!="F" and self.chegrade!="F" and self.biograde!="F":
                if self.mathgpa>=2.0:
                    result = ( res + self.biogpa + ( self.mathgpa - 2 ) ) / 6
                else:
                    result = ( res + self.biogpa ) / 6
            else:
                result = 0.00
        elif self.fourthsub=="127":
            if self.bangrade!="F" and self.enggrade!="F" and self.ictgrade!="F" and self.phygrade!="F" and self.chegrade!="F" and self.mathgrade!="F":
                if self.biogpa>=2.0:
                    result = ( res + self.mathgpa + ( self.biogpa - 2 ) ) / 6
                else:
                    result = ( res + self.mathgpa ) / 6
            else:
                result = 0.00
        
        if result>=5.00:
            self.resultGpa = 5.00
        else:
            self.resultGpa = result
        
    def calResultGrade(self):
        # calculate result grade
        if self.resultGpa>=5.0:
            self.resultGrade = "A+"
        elif self.resultGpa<5.0 and self.resultGpa>=4.0:
            self.resultGrade = "A"
        elif self.resultGpa<4.0 and self.resultGpa>=3.50:
            self.resultGrade = "A-"
        elif self.resultGpa<3.50 and self.resultGpa>=3.0:
            self.resultGrade = "B"
        elif self.resultGpa<3.0 and self.resultGpa>=2.0:
            self.resultGrade = "C"
        elif self.resultGpa<2.0 and self.resultGpa>=2.5:
            self.resultGrade = "D"
        else:
            self.resultGrade = "F"
            
    def getContent(self):
        root = "text/css"
        content = f'<!DOCTYPE html><html><head><title></title><link rel=\"stylesheet\" type=\"text/css\" href=\"style/style.css\">'+ f'</head><body><div class="container"><div class="heading"><h2>Omicon Coaching Center</h2><h4>Rajbari Hat, Manda, Naogaon, 01000000000</h4></div><div class="titleclass"><h1>HSC Final Model Test 2020</h1></div><div class="intro"><table class="intro"><tr><td>Roll no</td><td>:</td><td>{self.roll}</td></tr><tr><td>Student Name</td><td>:</td><td>{self.name}</td></tr><tr><td>C/O</td><td>:</td><td>{self.co}</td></tr><tr><td>Session</td><td>:</td><td>{self.session}</td></tr><tr><td>Phone</td><td>:</td><td>{self.phone}</td></tr><tr><td>Collage</td><td>:</td><td>{self.collage}</td></tr><tr><td>Fourth Subject</td><td>:</td><td>{self.fourthsub}</td></tr></table></div>'+ f'<div  class="mark"><h3 class="marktitle">Marksheet</h3><table class="mark" style="border-collapse: collapse;border: 1px solid black;"><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">Course Code</td><td style="border-collapse: collapse;border: 1px solid black;">Course Title</td><td style="border-collapse: collapse;border: 1px solid black;">Marks (CQ+MCQ+Practical)</td><td style="border-collapse: collapse;border: 1px solid black;">Total Marks</td><td style="border-collapse: collapse;border: 1px solid black;">GPA</td><td style="border-collapse: collapse;border: 1px solid black;">Grade</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">101</td><td style="border-collapse: collapse;border: 1px solid black;">Bangla 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.ban1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.bantotal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.bangpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.bangrade}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Bangla 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.ban2}</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">English 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.eng1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.engtotal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.enggpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.enggrade}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">English 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.eng2}</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">ICT</td><td style="border-collapse: collapse;border: 1px solid black;">{self.ict}</td><td style="border-collapse: collapse;border: 1px solid black;">{self.icttotal}</td><td style="border-collapse: collapse;border: 1px solid black;">{self.ictgpa}</td><td style="border-collapse: collapse;border: 1px solid black;">{self.ictgrade}</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">101</td><td style="border-collapse: collapse;border: 1px solid black;">Physics 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.phy1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.phytotal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.phygpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.phygrade}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Physics 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.phy2}</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Chemistry 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.che1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.chetotal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.chegpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.chegrade}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Chemistry 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.che1}</td></tr>'+ f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Higher Math 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.math1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.mathtotal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.mathgpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.mathgrade}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Higher Math 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.math1}</td></tr>'+f'<tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Biology 1st</td><td style="border-collapse: collapse;border: 1px solid black;">{self.bio1}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.biototal}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.biogpa}</td><td rowspan="2" style="border-collapse: collapse;border: 1px solid black;">{self.biograde}</td></tr><tr style="border-collapse: collapse;border: 1px solid black;"><td style="border-collapse: collapse;border: 1px solid black;">102</td><td style="border-collapse: collapse;border: 1px solid black;">Biology 2nd</td><td style="border-collapse: collapse;border: 1px solid black;">{self.bio2}</td></tr>'+f'<tr style="border-collapse: collapse;border: 1px solid black;"><td colspan="3" style="text-align: right;"></td><td style="border-collapse: collapse;border: 1px solid black;"><b>Result</b></td><td style="border-collapse: collapse;border: 1px solid black;"><b>{self.resultGpa}</b></td><td style="border-collapse: collapse;border: 1px solid black;"><b>{self.resultGrade}</b></td></tr></table></div>'+ f'<div><br><br><i style="padding-left: 30px;">Technical Support : Suvash Kumar, CSE, RU, http://suvash.unaux.com</i><br><br></div></div></body></html>'
        return content