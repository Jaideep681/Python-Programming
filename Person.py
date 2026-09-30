#Person Details

class Person:
    def __init__(self, name, age, city):
        self.name=name
        self.age=age
        self.city=city
p1=Person("Jaideep", 19, "Faridabad")   #p1=Person("Jaideep", "19", "Faridabad")
print(p1.name)
print(p1.age)
print(p1.city)
