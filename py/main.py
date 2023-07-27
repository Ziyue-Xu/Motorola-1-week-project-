import sqlite3 
import cgi
# ---------------------------------------------------------------------------- #
def get_info():
    
    #TODO -  get info from website 
    form = cgi.FieldStorage()
    first =  form.getvalue('first name')
    last =  form.getvalue('last name')
    age = form.getvalue('age')
    animal_bit =  form.getvalue('animal bit')
    trouble_breathing = form.getvalue("trouble breathing")
    coughing = form.getvalue("coughing")
    headache = form.getvalue("headache")
    rash = form.getvalue("rash")
    fever = form.getvalue("fever")
    vision_problems = form.getvalue("vision problems")
    current_medication= form.getvalue("current medication")
    known_conditions  = form.getvalue("known conditions")
    loss_of_appetite = form.getvalue("loss of appetite")
    # ---------------------------------------------------------------------------- #
    
    name =f"{first} {last}" 
    syptomns = f",{animal_bit}, {trouble_breathing}, {coughing}, {headache}, {rash}, {fever}, {vision_problems}, {current_medication}, {known_conditions},{loss_of_appetite}"
    curser.execute("INSERT INTO Patient(name, age, syptomns) VALUES (?, ?, ?);",(name, age, syptomns))

conc = sqlite3.connect("sql databases/hospital.db")
curser = conc.cursor()


data = []


get_info()


