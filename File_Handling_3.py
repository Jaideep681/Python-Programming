#FILE HANDLING 3

import csv
data=[{"Name":"Alice", "Score":85},{"Name": "Bob", "Score":92},{"Name": "Charlie", "Score":78}]

#Writing to csv

with open("grades.csv","w", newline="") as f:
    writer=csv.DictWriter(f, fieldnames=["Name", "Score"])
    writer.writeheader()
    writer.writerows(data)

#Reading it back

with open("grades.csv","r", newline="") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} scored {row['Score']}")
