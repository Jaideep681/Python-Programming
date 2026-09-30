#FILE HANDLING 2

lines=["First line\n", "Second line\n"]
with open("new_file.txt", "w") as file:
    file.write("Hello World!\n")
    file.writelines(lines)
