import sqlite3 
import cgi
# ---------------------------------------------------------------------------- #
def get_info():
    
    #TODO -  get info from website 
    form = cgi.FieldStorage()
    first =  form.getvalue('first name')
    last =  form.getvalue('last name')
    age = form.getvalue('age')
    fever = form.getvalue('Are you having a fever?')
    painSwallowing =  form.getvalue('Are you having pain when swallowing')
    soreThroat= form.getvalue("Are you having a sore throat?")
    swollen_tonsils = form.getvalue("Are you having Red and Swollen tonsils?")
    white_pathces_on_tonsils  = form.getvalue("Are you having white patches of pus on tonsils?")
    red_spots = form.getvalue("Are you having tiny red spots on the roof of the mouth?")
    swollen_lymp_node  = form.getvalue("Are you having a swollen lymph node?")
    # ---------------------------------------------------------------------------- #
    
    name =f"{first} {last}" 
    syptomns = f",{fever}, {painSwallowing}, {soreThroat}, {swollen_tonsils}, {white_pathces_on_tonsils}, {red_spots}, {swollen_lymp_node}"
    curser.execute("INSERT INTO Patient(name, age, syptomns, analyzed) VALUES (?, ?, ?, 1);",(name, age, syptomns))

conc = sqlite3.connect("data/hospital.db")
curser = conc.cursor()

get_info()


