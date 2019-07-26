import os.path
import sys
import time


#opens file
path = "C:\PythonDrill"
dirs = os.listdir(path)


#this will print all files in directory
for file in dirs:
    print(file)
  

#this sets the fName fPath variables 
    fName = '\nPythonDrill_V1.txt, \nPythonDrill_V2.txt, \nPythonDrill_V3.txt, \nPythonDrill_V4.txt, \nPythonDrill_V5.txt, \nPythonDrill_V6.txt, \nPythonDrill_V7.txt, \nPythonDrill_V8.txt, \nPythonDrill_V9.txt. \nPythonDrill_V10.txt'

    fPath = '\nC:\\PythonDrill\\'
#this joins the path and the respective files 
    pythonPath = os.path.join(fPath, fName)


print(pythonPath)

#this block will print the latest date that each text file was modififed
modification_Epoc = os.path.getmtime('C:\PythonDrill')
modification_Time = time.strftime('%H:%M:%S', time.localtime(modification_Epoc))

print("\nLast modification time:", modification_Time)

