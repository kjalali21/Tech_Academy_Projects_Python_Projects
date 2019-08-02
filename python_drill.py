import os.path
import sys
import time
import os


#opens file & set variables 
path = "C:\\PythonDrill"
fName = '.txt'
modification_Epoc = os.path.getmtime("C:\\PythonDrill")
dirs = os.listdir(path)

#this will print all files in directory
for file in dirs:
    print(file)
  

# this only will list .txt files in PythonDrill directory
for file in os.listdir(path):
    if file.endswith(fName):
        modification_Epoc = os.path.getmtime(os.path.join(path,file))
        modification_Time = time.strftime('%H:%M:%S', time.localtime(modification_Epoc))   
        print(f'{file}, {modification_Time}')
