#Exception Handling

try:
    number=int(input("Enter your integer number to divide by 10: "))
    result=10/number
    print(f"Result is {result}")
except ZeroDivisionError:
    #Runs if you are trying to divide by zero
    print("Error: Can't divide by zero")
except ValueError:
    #Runs if passes string value to number
    print("Error: Enter a valid number")
