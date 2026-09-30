#FILE HANDLING 1

#Writing to a file

f=open("sample.txt","w")
f.write("Hello, this is a file handling example in Python.")
f.close()

#Reading from a file

f=open("sample.txt","r")
print("File Content: ")
print (f.read())
f.close()
