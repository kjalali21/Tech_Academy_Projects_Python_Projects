import os.path
import sys
import time


#opens file & set variables 
path = "C:\\PythonDrill"
fName = '.txt'
modification_Epoc = os.path.getmtime("C:\\PythonDrill")
dirs = os.listdir(path)

#this will print all files in directory
for file in dirs:
    print(file)
  

#this joins the path and the respective files 
pythonPath = os.path.join(path,fName)
print(pythonPath)

# this only will list .txt files in PythonDrill directory
for file in os.listdir(path):
    if file.endswith(fName):
     print(path + fName,modification_Epoc)
