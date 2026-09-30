#Write a Python function to sum all the numbers in a list.

#To print sum of all numbers in a list using function

def list_sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum
numbers=[1,2,3,4,5]
print("Sum of all items which is present in the list is",list_sum(numbers))
