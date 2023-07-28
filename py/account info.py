import sqlite3
import cgi

conc = sqlite3.connect("data/hospital.db")
curser = conc.cursor()

name = cgi.FieldStorage()

if requst == True:
    curser.execute("SELECT * FROM Personal_account WHERE Name = ?;",(name, ))
