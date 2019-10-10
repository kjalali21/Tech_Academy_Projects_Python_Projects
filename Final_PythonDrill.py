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
       

     ###Source Directory Button sets your source folder path 
        def source_directory():
            source_path.set( filedialog.askdirectory() ) ## function returns the source folder path 
        
            
    #####Destination dierctory button sets your destination folder path
        def dest_directory():
            destination_path.set( filedialog.askdirectory() ) ## Function returns the destination folder path 

        def quit():
           global root
           root.quit() ## destroys tkinter window
          

        def iterate_directory():
            for file in os.listdir( source_path.get() ): ## look for a file in the source_path folder and return the value of the variable as a string.  
                if file.endswith('.txt'): ## if the file is a .txt file 
                    connection = sqlite3.connect('Final_PythonDrill1.db')  # connect to the sqlite3 database called 'Final_PythonDrill1.db'     
                    shutil.move( os.path.join(source_path.get(),file),(destination_path.get()) ) # move chosen source_path if they are/or have .txt files into destination_path. 
                    destination_mtime = os.path.getmtime(os.path.join(destination_path.get(),file)) # grabs the last time the files were modifed that were moved to destination_path, in this case when it is moved. 
                    destination_local = time.strftime('%H:%M:%S',time.localtime (destination_mtime)) #converts the tuple into a string & displays local time with Hour, Minutes and Seconds. Takes destination_mtime instance for when they were modfied.  
                    with connection: ## with the sqlite3 database "Final_PythonDrill1.db"
                        cur = connection.cursor() ## once connected to database, return a cursor.
                        cur.execute ("CREATE TABLE IF NOT EXISTS tbl_filepaths( \
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                                fname TEXT, \
                                Mtime TEXT )")
                        cur.execute("INSERT INTO tbl_filepaths(fname,Mtime) VALUES (?,?)", (file,destination_mtime))  ### 44-49. execute the cursor that is connected to the database, and create a table with those column names if it does not already exist. 
                        connection.commit() ## commit all values in the database 
                    connection.close() ## close the database.                          

                    print(file,(destination_local))




         
                                
        
   
        #building master frame parameters
        self.master = master
        self.master.minsize(500,150)
        self.master.maxsize(500,300)
        #title of window
        self.master.title("Master File Browser")
        self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...',command=source_directory) ### command grabs the function being used. 
        self.btn_browse.grid(row=3,column=0,padx=(15,5),pady=(25,0),sticky=N+W)
        self.btn_browse_1 = tk.Button(self.master,width=12,height=1,text='Browse...', command=dest_directory)
        self.btn_browse_1.grid(row=4,column=0,padx=(15,5),pady=(10,0),sticky=N+W)
        self.btn_browse_2 = tk.Button(self.master,width=12,height=2,text='Check for Files...', command=iterate_directory)
        self.btn_browse_2.grid(row=5,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program', command=quit) ## create close program function 
        self.btn_close.grid(row=5,column=2,padx=(270,0),pady=(10,0),sticky=E)


        self.txt_fname = tk.Entry(self.master,text='hello',textvariable=source_path)
        self.txt_fname.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(25,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='',textvariable=destination_path)
        self.txt_lname.grid(row=4,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(15,0),sticky=N+E+W) 







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
