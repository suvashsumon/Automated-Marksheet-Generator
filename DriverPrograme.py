import sqlite3

database_name = "database.db"
conn = sqlite3.connect(database_name)
data = conn.execute("SELECT * FROM FinalModelTest;")
for row in data:
    print(row)
    
conn.close()