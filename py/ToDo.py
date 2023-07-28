import sqlite3
import sqlite


conc = sqlite3.connect("data/hospital.db")
curser = conc.cursor()
def getnurse(pred_problem):
     for r in range(5):
        curser.execute("SELECT Name FROM Personal WHERE Busy == 0;")
        asigned = curser.fetchone()
        curser.execute("UPDATE Patient SET nurse= ? WHERE nurse == NULL AND WHERE status = ?;",(asigned,r))
        curser.execute("SELECT Name FORM Patient WHERE nurse == ?;",(asigned,))
        assigned = curser.fetchone()
        return assigned
def getDoc(pred_problem):
    for r in range(5):
        curser.execute("SELECT FROM Personal WHERE Busy == 0 AND WHERE expertise == ?;",(pred_problem,))
        asigned = curser.fetchone()
        curser.execute("UPDATE Patient SET docter = ? WHERE docter == NULL AND WHERE status = ?;",(asigned,r))
        curser.execute("SELECT current room FORM Patient WHERE docter == ?;",(asigned,))
        assigned = curser.fetchone()
        return assigned
        


        