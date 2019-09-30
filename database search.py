import sqlite3
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
from tkinter import*
from functools import partial  


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
 
def select_task_by_priority(a,b,c):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("test")

    
    cur = conn.cursor()
    cur.execute("SELECT Partnumber,Colorname,L,A,B FROM reading ")
    rows = cur.fetchall()
    color1=LabColor(lab_l=L, lab_a=A, lab_b=B)
    for row in rows:
        color2=LabColor(lab_l=row[2], lab_a=row[3], lab_b=row[4])
        if(delta_e_cie1976(color1, color2)<3):
            print(row[0]," ",row[1])
    

def main():
    database = r"C:\Users\icarus\python\ScanDatabase.db"
 
    # create a database connection
    conn = create_connection(database)
    root=Tk()
    root.geometry("250x250")
    
    with conn:
        L = Label(root, text = "Enter your L reading: ")
        L.grid(row = 1, column = 0, padx = 0, pady = 10)
        e1 = Entry(root)
        e1.grid(row = 1, column = 1, padx = 0, pady = 10)
        a=e1.get()

        
        A = Label(root, text ="Enter your A reading: ")
        A.grid(row = 2, column = 0, padx = 0, pady = 10)
        e2 = Entry(root)
        e2.grid(row = 2, column = 1, padx = 0, pady = 10)
        b=e2.get()
    
        B = Label(root, text = "Enter your B reading: ")
        B.grid(row = 3, column = 0, padx = 0, pady = 10)
        e3 = Entry(root)
        e3.grid(row = 3, column = 1, padx = 0, pady = 10)
        c=e3.get()

        
        select_task_by_priority=partial(conn,a,b,c)
        sbmitbtn = Button(root, text = "Submit",activebackground = "pink", activeforeground = "blue",command=lambda color1:self.select_task_by_priority(a,b,c))
        sbmitbtn.grid(row = 4, column = 0, padx = 0, pady = 10)
       
 
    root.mainloop() 
if __name__ == '__main__':
    main()
