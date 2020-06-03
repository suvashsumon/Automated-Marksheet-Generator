from Marksheet import *
import sqlite3

database_name = "database.db"
conn = sqlite3.connect(database_name)
data = conn.execute("SELECT * FROM FinalModelTest;")
for row in data:
    student = Marksheet(row)
    #student.show()
    student.setTotal()
    #student.checkTotal()
    student.setGpa()
    #student.checkGpa()
    student.setGrade()
    #student.checkGrade()
    student.calResultGpa()
    student.calResultGrade()
    file = "Marksheets/" + student.roll + ".html"
    with open(file,"w") as sheet:
        sheet.write(student.getContent())
        print(f"{student.roll} Done")
    
conn.close()