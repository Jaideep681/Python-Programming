#Class property vs Object property

class Person:
    species="Human"                 #class property
    def __init__(self,name):
        self.name=name              #instance property
p1=Person("Rahul")
p2=Person("Pankaj")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
