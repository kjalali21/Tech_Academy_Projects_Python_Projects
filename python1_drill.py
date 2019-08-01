import os.path
import sys
import time


#opens file
path = "C:\\"
dirs = os.listdir(path)


#this will print all files in directory
for file in dirs:
    print(file)
  

#this sets the fName fPath variables 
    fName = '.txt'
    
    fPath = '\nC:\\'
#this joins the path and the respective files 
    pythonPath = os.path.join(fPath, fName)

# this only will list .txt files in PythonDrill directory
for file in os.listdir('C:\\'):
    if file.endswith(".txt"):
        print(os.path.join('C:\\', file))

print(pythonPath)

#this block will print the latest date that each text file was modififed
modification_Epoc = os.path.getmtime('C:\\')
modification_Time = time.strftime('%H:%M:%S', time.localtime(modification_Epoc))


print("\nLast modification time:", modification_Time)