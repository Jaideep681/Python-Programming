#Import for Abstraction
from abc import ABC,abstractmethod

#Make Parent Class
class Person(ABC):
    
    #Making Constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #Display Name and Age of Student
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

    #Using abstractionmethod from import
    @abstractmethod
    def get_role(self):
        pass

#Make Child Class
class Student(Person):
    
    #Making Constructor
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.__marks=marks                  #Encapsulation (Private)
        
    #Getter function
    def get_marks(self):
        return self.__marks
    
    #Setter function
    def set_marks(self,marks):
        self.__marks=marks
        
    #Calculation of Average Marks 
    def cal_avg(self):
        total=sum(self.__marks)
        avg=total/len(self.__marks)
        return avg
    
    #Display Result
    def display_result(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Average:",self.cal_avg())
        if(self.cal_avg()>=40):
            print("Result: Pass")
        else:
            print("Result: Fail")
            
    #Polymorphism
    def display(self):
        super().display()
        print("Rollno:",self.rollno)
        print("Marks:",self.__marks)
        
    #Abstraction
    def get_role(self):
        return "Student"

#Menu-Driven Program
students=[]
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Display Result")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        rollno=int(input("Enter your roll number: "))
        marks=list(map(int,input("Enter your marks: ").split()))
        s=Student(name,age,rollno,marks)
        students.append(s)
        print("Student Added!\n")
        
    elif choice==2:
        if not students:
            print("Student is not added, firstly add the student!!")
        else:
            for s in students:
                s.display()
                
    elif choice==3:
        if not students:
            print("Student is not added, firstly add the student!!")
        else:
            for s in students:
                s.display_result()
                
    elif choice==4:
        print("Exiting...\n")
        break
    
    else:
        print("Invalid Choice, please try again...\n")
