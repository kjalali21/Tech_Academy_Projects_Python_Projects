 #building master frame parameters
from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)    
    
    
    
    def gui_loaded(self):    

   
    
        
    self.master = master
    self.master.minsize(500,150)
    self.master.maxsize(500,300)
        #title of window
    self.master.title("Master File Browser")
    self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse.grid(row=3,column=0,padx=(15,5),pady=(25,0),sticky=N+W)
    self.btn_browse_1 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse_1.grid(row=4,column=0,padx=(15,5),pady=(10,0),sticky=N+W)
    self.btn_browse_2 = tk.Button(self.master,width=12,height=2,text='Check for Files...')
    self.btn_browse_2.grid(row=5,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=5,column=2,padx=(270,0),pady=(10,0),sticky=E)


    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(25,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=4,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(15,0),sticky=N+E+W) 


