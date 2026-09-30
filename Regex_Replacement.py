import re
text="Dog is Cute!"
pattern="Dog"
replacement="Cat"
replace=re.sub(pattern,replacement,text)
if replace:
    print("The given text is replaced by another text!")
    print(f"Replaced text: {replace}")
else:
    print("The text isn't replaced by another text!")
