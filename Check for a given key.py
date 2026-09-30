#Write a Python script to check if a given key already exists in a dictionary.

#Program to check if a given key already exists in a dictionary

my_dict={1:"Apple",2:"Banana",3:"Mango"}
key=int(input("Enter key to check: "))
if key in my_dict:
    print("Key exists")
else:
    print("Key doesn't exists")
