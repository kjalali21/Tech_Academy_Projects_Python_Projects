import sqlite3
connection = sqlite3.connect('Drill_5.db')

# Variables for both file extension and files #

#filextension variable
fext = '.txt'

# array of files
files = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

###

#connects to sqlite3 and creates table 'all_files' with int as Primary Key #

with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_files( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      fname TEXT \
       )")
    connection.commit() 
connection.close()         

#creates if statement and uses variable 'fext'  
connection = sqlite3.connect('Drill_5.db')
with connection:
    cur = connection.cursor()       
    for i in files:
        if i.endswith(fext):
            msg = "files: {}".format(i) 
            print(msg)
            cur.execute("INSERT INTO all_files(fname) VALUES (?)", \
        (i,))      
            




