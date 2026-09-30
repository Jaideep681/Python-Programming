import re
text="My ally's email is test123@gamil.com"
pattern="\w+@\w+\.\w+"
validate=re.search(pattern,text).group()
if validate:
    print("The given E-mail ID is correct!!")
    print(f"E-mail ID is: {validate}")
else:
    print("The given E-mail ID is wrong!!")
