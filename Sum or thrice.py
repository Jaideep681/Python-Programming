'''Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum.'''

#Calculate sum of three numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
sum=(a+b+c)
if(a==b==c):
    print ("Result: ",sum*3)
else:
    print("Result: ",sum)
