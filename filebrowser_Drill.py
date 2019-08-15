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
        
        ### function for Browse Folder Button
        def opendirectory():
            global folder_path
            filename = filedialog.askdirectory()
            folder_path.set(filename)
            print(filename)

        self.browse = tk.Button(self.master,width=12,height=2,text="Browse Folders..",command=opendirectory)
        self.browse.grid(row=1,column=0,padx=(15,5),pady=(25,0),sticky=W)
        # GUI TextBox
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>',(self))
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=3,padx=(70,0),pady=(0,0),sticky=E)
        self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

        
        

        

    




        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()        