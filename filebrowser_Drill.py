from tkinter import *
from tkinter import filedialog
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
        global folder_path
        folder_path = StringVar()
        ### function for Browse Folder Button
        def opendirectory():
            
            dirname = filedialog.askdirectory()
            folder_path.set(dirname)
            print(dirname)
          
        ### lists file path in TK listbox    
        self.browse = tk.Button(self.master,width=12,height=1,text="Browse Folders..",command=opendirectory)
        self.browse.grid(row=1,column=0,padx=(5,5),pady=(25,0))
        # GUI ListtBox
        self.lstList1 = tk.Entry(self.master,text='',textvariable=folder_path)
        self.lstList1.bind('<<ListboxSelect>>',(self))
        self.lstList1.grid(row=2,column=1,rowspan=7,columnspan=5,padx=(45,30),pady=(0,0),sticky=N+E+W)

        
        


        

    




        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()        