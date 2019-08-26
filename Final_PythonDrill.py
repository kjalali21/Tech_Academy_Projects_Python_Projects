from tkinter import *
from tkinter import filedialog
import sqlite3
import os
import shutil
import glob
import time
import sys
import tkinter as tk 

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

#######Variables#######

        destination_path = StringVar()
        source_path = StringVar()
       

     ###Source Directory Button sets your source path 
        def source_directory():
            source_path.set( filedialog.askdirectory() )
        
            
    #####Destination dierctory button sets your destination path
        def dest_directory():
            destination_path.set( filedialog.askdirectory() )
          

        def iterate_directory():
            for file in os.listdir( source_path.get() ):
                if file.endswith('.txt'):
                    connection = sqlite3.connect('Final_PythonDrill1.db')           
                    shutil.move( os.path.join(source_path.get(),file),(destination_path.get()) )
                    destination_mtime = os.path.getmtime(os.path.join(destination_path.get(),file))
                    destination_local = time.strftime('%H:%M:%S',time.localtime (destination_mtime))
                    with connection:
                        cur = connection.cursor()
                        cur.execute ("CREATE TABLE IF NOT EXISTS tbl_filepaths( \
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                                fname TEXT, \
                                Mtime TEXT )")
                        cur.execute("INSERT INTO tbl_filepaths(fname,Mtime) VALUES (?,?)", (file,destination_mtime))  
                        connection.commit()
                    connection.close()                          

                    print(file,(destination_local))

      ##### 


         
                                
        
   
        #building master frame parameters
        self.master = master
        self.master.minsize(500,150)
        self.master.maxsize(500,300)
        #title of window
        self.master.title("Master File Browser")
        self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...',command=source_directory)
        self.btn_browse.grid(row=3,column=0,padx=(15,5),pady=(25,0),sticky=N+W)
        self.btn_browse_1 = tk.Button(self.master,width=12,height=1,text='Browse...', command=dest_directory)
        self.btn_browse_1.grid(row=4,column=0,padx=(15,5),pady=(10,0),sticky=N+W)
        self.btn_browse_2 = tk.Button(self.master,width=12,height=2,text='Check for Files...', command=iterate_directory)
        self.btn_browse_2.grid(row=5,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
        self.btn_close.grid(row=5,column=2,padx=(270,0),pady=(10,0),sticky=E)


        self.txt_fname = tk.Entry(self.master,text='hello',textvariable=source_path)
        self.txt_fname.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(25,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='',textvariable=destination_path)
        self.txt_lname.grid(row=4,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(15,0),sticky=N+E+W) 







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
