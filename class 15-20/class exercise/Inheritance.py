"""
1. Single Inheritance
2. Multiple Inher.
3. Multilevel Inher.
4. Hierachical Inher.
"""


# Single Inheritance

class ClassA:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isClassB(self):
        return False


# Class B  Inherit Class A [Class - B :: Child/Derived || Class - A :: Parent/Base]
class ClassB(ClassA):

    def isClassB(self):
        return True


classA = ClassA("Class-1")
print(classA.getName(), classA.isClassB())  # Class-1 False

classB = ClassB("Class-2")
print(classB.getName(), classB.isClassB())  # Class-2 True

