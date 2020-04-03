class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp1=Employee("Abhishek",11507151)
emp2=Employee("Alok",11507152)

emp1.display()
emp2.display()
