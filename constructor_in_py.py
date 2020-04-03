class Employee:  
    def __init__(self,name,id):  
        self.id = id;  
        self.name = name;  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp1 = Employee("John",101)  
emp2 = Employee("David",102)
emp3=Employee("Tanya",103)
  
#accessing display() method to print employee 1 information  
   
emp1.display();   
  
#accessing display() method to print employee 2 information  
emp2.display();

emp3.display()
