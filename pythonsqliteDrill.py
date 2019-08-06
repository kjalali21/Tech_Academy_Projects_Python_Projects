import sqlite3
connection = sqlite3.connect('Drill_2.db')

with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Drill( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      firstName TEXT \
      )")
    connection.commit() 
connection.close()         


connection = sqlite3.connect('Drill_2.db')

with connection:
    cur = connection.cursor()
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('data.pdf'))
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('Hello.txt'))    
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('information.docx'))     
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('myImage.png'))     
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('myMovie.png')) 
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('myPhoto.png'))       
    cur.execute("INSERT INTO Drill (firstName) VALUES (?)", \
        ('World.txt'))           
    connection.commit()
connection.close()    


connection = sqlite3.connect('Drill_2.db')
with connection:
    cur = connection.cursor()
    cur.execute("SELECT firstName FROM Drill WHERE firstName = '.txt' ")
    File = cur.fetchall
    for item in File:
        filemsg = "File Name: {}".format(item[0])
    print(filemsg)    


