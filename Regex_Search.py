import re
text="Science is experimental!"
pattern="Science"
search=re.search(pattern,text).group()
if search:
    print("The Pattern is found in the given text!")
    print(f"The word is {search}")
else:
    print("The Pattern is not found in the given text!")
