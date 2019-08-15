from tkinter import *
import tkinter as tk

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
         
        #building master frame parameters
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #title of window
        self.master.title("File Browser")
        

        self.browse = tk.Button(self.master,width=12,height=1,text="Browse" )
        self.browse = tk.Button(self.master,width=12,height=1,text="Browse" )
        #GUI BUTTON
        self.browse.grid(row=1,column=0,padx=(25,5),pady=(55,0),sticky=W)
        
        # GUI TextBox
        self.box = tk.Entry(self.master, text = '')
        self.box.grid(row=8,column=3,rowspan=1,columnspan=7,padx=(45,0),pady=(55,0),sticky=N+E+W)

        

    




        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()        