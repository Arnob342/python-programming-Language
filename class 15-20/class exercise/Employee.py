## ----------------------- Class - Start -----------------------------
class Employee:
    # self - refer to the specific object that is calling that functions

    ## ------------ Constructor Method - Start ---------------------------
    def __init__(self, name, age, salary, department, id):  # Creating a function - Constructor
        self.name = name
        self.age = int(age)
        self.salary = salary
        self.department = department
        self.id = id

    ## ------------ Constructor Method - End ---------------------------

    ## Method - Start
    def getEmployeeName(self):
        return self.name
    ## Method - End


## ----------------------- Class - End -----------------------------

# Employee - Object Create
emp1 = Employee("Emp1", 24, 50000, "IT", 'AA')

emp1.name = "Emp3"
# print(emp1.__dict__)
print(emp1.getEmployeeName())

emp2 = Employee("Emp2", 30, 40000, "Account", 67890)
# print(emp2.__dict__)
print(emp2.getEmployeeName())
"""
1/ Class
2/ Object
3/ Self
4/ Constructor
5/ Method 
"""
