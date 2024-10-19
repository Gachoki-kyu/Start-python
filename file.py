# file handling in python
f = open("demo.txt", "r")
#print(f.read())  #reads the file
print(f.readline()) # reads the first line of the file
print(f.readline()) # reads the second line
f.close()

# wrtting in file
x = open("demo.txt", 'a')
x.write("added some new content to the file ")
x.close()
#open the file
x = open("demo.txt", "r")
print(x.read())
x.close()

#deleting a file
import os
try:
    os.remove("numpy.py")
except:
    print("file does not exist")