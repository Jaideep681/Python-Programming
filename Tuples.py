#WAP to implement tuples in Python

#1.Create a tuple
fruits_tuple=("Apple","Banana","Cherry","Papaya")

#2.Accessing tuple element
print(f"First fruit: {fruits_tuple[0]}")
print(f"Last fruit: {fruits_tuple[-1]}")

#3.Checking the length
print(f"Number of items: {len(fruits_tuple)}")

#4.Iterating a tuple
for index,fruit in enumerate(fruits_tuple):
    print(f"{index+1}. {fruit}")

#5.Concatenating tuples
more_fruits=("Mango","Strawberry","Watermelon")
all_fruits=fruits_tuple+more_fruits
print(f"Joined tuple: {all_fruits}")

#6.Unpacking a tuple
f1,f2,f3,f4=fruits_tuple
print(f"Unpacked values: {f1}, {f2}, {f3}, {f4}")
