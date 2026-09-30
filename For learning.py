#For learning

list1=[1,2,3]
list2=[4,5,"RAHUL"]
list3=list1+list2
print(list3)
list4=[7,8,9]
list3.extend(list4)
print(list3)
list3.insert(9,10)
print(list3)
list3.append(11)
print(list3)
del list3[10]
print(list3)
del list3[1:4]
print(list3)
list3.remove(8)
print(list3)
list3.pop()
print(list3)
list3.clear()
print(list3)
my_profiles={'Name':'Rahul','Age':20,'E-mail':'abc@gmail.com','Contact no.':9810504681}
print(my_profiles)
print(my_profiles['Age'])
my_profiles['City']='New York'
print(my_profiles)
del my_profiles["Age"]
print(my_profiles)
print(my_profiles.keys())
print(my_profiles.values())
