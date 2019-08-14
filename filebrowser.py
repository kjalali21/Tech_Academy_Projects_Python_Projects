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
        

        #GUI 
    def gui_widgets(self): 
        self.browse = Button(self.master, text width=12,height=2 text="Browse" )





        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()        