import sqlite3
import cgi
conc = sqlite3.connect("sql databases/hospital.db")
curser = conc.cursor()

form = cgi.FieldStorage()

def room_config():
    room_num =  form.getvalue('room num')
    section =  form.getvalue('section')
    location = form.getvalue('location')
    curser.execute("INSERT INTO Hospital_map(room_num, section, location) VALUES(?,?,?)",(room_num,section,location))

def perosnal_config():
    name = form.getvalue("name")
    feild_of_study = form.getvalue("feild of study")
    number = form.getvalue("number")  


if form.getvalue("config") == "room":
    room_config()
else:
    perosnal_config()