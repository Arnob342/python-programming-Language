class Employee:
    def __init__(self,name):
        self.name = name
    def display (self):
        print('The name of employee is:',self.name)

first = Employee('arnob')
second = Employee('reduan')

second.display()