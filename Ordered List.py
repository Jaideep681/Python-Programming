#Ordered list implementation
class OrderedList():
    def __init__(self):     #Simple Constructor
        self.items=[]
    def insert(self,item):
        i=0
        while(i<len(self.items) and self.items[i]<item):
            i+=1        #Valid Syntax    #i++(Invalid Syntax)       
        self.items.insert(i,item)
    def display(self):
        print("Ordered list:",self.items)
#Main function
        
ol=OrderedList()
ol.insert(30)
ol.insert(10)
ol.insert(20)
ol.insert(5)
#Display ordered list

ol.display()
