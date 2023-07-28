import sqlite3
import pickle
conc = sqlite3.connect("data/hospital.db")
curser = conc.cursor()
 
curser.execute("SELECT syptomns FROM Patient WHERE analyzed = 0;")
data = curser.fetchone()

labs = ["transfusion","toxacolagy", "cheminsty", "hemotolagy", "emunolagy", "micro_bio", "cytology"]

#NOTE - sudo code below
diagnoses = model.predict(data)

 #TODO - here is where you  look through all of your opsions 

