class Employee:
    empcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displayCount(self):
        print (f"total employee {Employee.empcount}")

    def displayEmployee(self):
        print ("name : " , self.name , ",salary : " , self.salary)

emp1 = Employee("bena",2000)
emp2 = Employee('gachoki', 50000)

emp1.displayEmployee()
emp2.displayEmployee()
print( f"total employees {Employee.empcount}")