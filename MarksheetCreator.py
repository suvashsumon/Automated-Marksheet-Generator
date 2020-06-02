import sqlite3

class Marksheet:
    ba1 = ""
    ba2 = ""
    e1 = ""
    e2 = ""
    ict = ""
    p1 = ""
    p2 = ""
    c1 = ""
    c2 = ""
    h1 = ""
    h2 = ""
    b1 = ""
    b2 = ""
    fourth = ""
    content = ""
    totalmark = []
    gpa = []
    grade = []
    def getSum(self, rawmark):
        raw = rawmark.split(rawmark)
        s = 0
        for i in raw:
            s = s + int(i)
            
        return s
    
    def getGpa(self,m):
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
    
    def getGrade(self,m):
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
    
    def appendlist(self,ba1,ba2,e1,e2,ict,p1,p2,c1,c2,h1,h2,b1,b2,fourth):
        #updating mark list
        mark.append(ba1)
        mark.append(ba2)
        mark.append(e1)
        mark.append(e2)
        mark.append(ict)
        mark.append(p1)
        mark.append(p2)
        mark.append(c1)
        mark.append(c2)
        mark.append(h1)
        mark.append(h2)
        mark.append(b1)
        mark.append(b2)
        
        #updating totalmark list
        totalmark.append(getSum(ba1)+getSum(ba2))
        totalmark.append(getSum(e1)+getSum(e2))
        totalmark.append(getSum(ict))
        totalmark.append(getSum(p1)+getSum(p2))
        totalmark.append(getSum(c1)+getSum(c2))
        totalmark.append(getSum(h1)+getSum(h2))
        totalmark.append(getSum(b1)+getSum(b2))
        
        #updating gpa list
        gpa.append(getGpa(getSum(ba1)+getSum(ba2)))
        gpa.append(getGpa(getSum(e1)+getSum(e2)))
        gpa.append(getGpa(getSum(ict)))
        gpa.append(getGpa(getSum(p1)+getSum(p2)))
        gpa.append(getGpa(getSum(c1)+getSum(c2)))
        gpa.append(getGpa(getSum(h1)+getSum(h2)))
        gpa.append(getGpa(getSum(b1)+getSum(b2)))
        
        #updating grade list
        grade.append(getGrade(getSum(ba1)+getSum(ba2)))
        grade.append(getGrade(getSum(e1)+getSum(e2)))
        grade.append(getGrade(getSum(ict)))
        grade.append(getGrade(getSum(p1)+getSum(p2)))
        grade.append(getGrade(getSum(c1)+getSum(c2)))
        grade.append(getGrade(getSum(h1)+getSum(h2)))
        grade.append(getGrade(getSum(b1)+getSum(b2)))
    
    def calResult(self):
        sg = 0
        for i in gpa:
            sg += int(int(i))
        
        if fourth=="":
            sg = int(gpa[])
        
        return sg
    
    def calGpa(self):
        res = calResult()
        if calResult()>:
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
        
    def getStart(self):
        #con = sqlite3.connect("database.db")
        #con.close()
        appendList()