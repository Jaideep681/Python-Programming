def check_age(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    elif age<18:
        print("Access denied!")
    else:
        print("Access granted!")
try:
    age=int(input("Enter your age: "))
    check_age(age)
except ValueError as ve:
    print(f"Error: Custom Error {ve}")
