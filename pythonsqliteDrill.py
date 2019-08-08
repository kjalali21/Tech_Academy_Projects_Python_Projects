import sqlite3
connection = sqlite3.connect('Drill_5.db')

#filextension variable
fext = '.txt'

# array of files
files = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_files( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      fname TEXT \
       )")
    connection.commit() 
connection.close()         

  
connection = sqlite3.connect('Drill_5.db')
with connection:
    cur = connection.cursor()       
    for item in files:
        if item.endswith(fext):
            msg = "files: {}".format(item) 
            print(msg)
            cur.execute("INSERT INTO all_files(fname) VALUES (?)", \
        (item,))      
            




