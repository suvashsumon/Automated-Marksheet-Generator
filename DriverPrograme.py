from Marksheet import *
import sqlite3

database_name = "database.db"
conn = sqlite3.connect(database_name)
data = conn.execute("SELECT * FROM FinalModelTest;")
for row in data:
    student = Marksheet(row)
    student.show()
    student.setTotal()
    student.checkTotal()
    student.setGpa()
    student.checkGpa()
    student.setGrade()
    student.checkGrade()
    student.calResultGpa()
    student.calResultGrade()
    print(f"result is : {student.resultGpa}")
    print(f"result is : {student.resultGrade}")
    print()
    
conn.close()