#Build a simple grade calculator

math=int(input("Enter your maths marks: "))
eng=int(input("Enter your english marks: "))
evs=int(input("Enter your evs marks: "))
ssc=int(input("Enter your ssc marks: "))
hindi=int(input("Enter your hindi marks: "))
total_marks=math+eng+evs+ssc+hindi
perc=(total_marks)/5
if(perc>=90):
    print("Your grade: A")
elif(perc>=80):
    print("Your grade: B")
elif(perc>=70):
    print("Your grade: C")
elif(perc>=60):
    print("Your grade: D")
elif(perc>=50):
    print("Your grade: E")
else:
    print("Fail")
print(f"Your Total marks: {total_marks}")
