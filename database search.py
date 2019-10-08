import sqlite3
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
import tkinter as tk
from functools import partial  
from functools import reduce
from tkinter import messagebox
import pandas as pd 

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
 
 
 
def select_task_by_priority(conn,L,A,B,Delta):
    result=[]
    df = pd.DataFrame(result, columns = ['Part Number', 'Color Name','Delta-E'])
    del df.index.name 


    cur = conn.cursor()
    cur.execute("SELECT Partnumber,Colorname,L,A,B FROM reading ")
    rows = cur.fetchall()
    color1=LabColor(lab_l=L, lab_a=A, lab_b=B)
    for row in rows:
        color2=LabColor(lab_l=row[2], lab_a=row[3], lab_b=row[4])
        if(delta_e_cie1976(color1, color2)<Delta):
            Delta_E=str(round(delta_e_cie1976(color1, color2),2))
            df2={'Part Number':row[0], 'Color Name':row[1],'Delta-E':Delta_E}
            df=df.append(df2,ignore_index=True)
    df.sort_values("Delta-E",ascending=True, inplace=True)
    print (df)

    


def getcolor(conn,light,red,blue,delta):
    L=light.get()
    A=red.get()
    B=blue.get()
    Delta=delta.get()

   

    L=float(L)
    A=float(A)
    B=float(B)
    Delta=float(Delta)
    select_task_by_priority(conn,L,A,B,Delta)
    
def main():
    database = r"C:\Users\icarus\python\ScanDatabase.db"
 
    # create a database connection
    conn = create_connection(database)
    root= tk.Tk()
    root.geometry("250x250")
    



    L = tk.Label(root, text = "Enter your L reading: ")
    L.grid(row = 1, column = 0, padx = 0, pady = 10)
    light =tk.Entry(root)
    light.grid(row = 1, column = 1, padx = 0, pady = 10)
  
        

    A = tk.Label(root, text ="Enter your A reading: ")
    A.grid(row = 2, column = 0, padx = 0, pady = 10)
    red = tk.Entry(root)
    red.grid(row = 2, column = 1, padx = 0, pady = 10)
    
      
    
    B = tk.Label(root, text = "Enter your B reading: ")
    B.grid(row = 3, column = 0, padx = 0, pady = 10)
    blue = tk.Entry(root)
    blue.grid(row = 3, column = 1, padx = 0, pady = 10)

    D = tk.Label(root, text = "Enter your Delta-E reading: ")
    D.grid(row = 4, column = 0, padx = 0, pady = 10)
    delta = tk.Entry(root)
    delta.grid(row = 4, column = 1, padx = 0, pady = 10)
 
       
    sbmitbtn = tk.Button(root, text = "Submit",command=lambda: getcolor(conn,light,red,blue,delta))
    sbmitbtn.grid(row = 5, column = 0, padx = 0, pady = 10)
       
 
    root.mainloop() 
if __name__ == '__main__':
    main()
