""""
A -> B
A -> C
B -> C
"""


# Base/Parent Class
class A:
    def subtration(self, num1, num2):
        return num1 - num2

    def Addtion(self, num1, num2):
        return num1 + num2


# Child/Derived
class B(A):
    def multi(self, num1, num2):
        return num1 * num2


# Child/Derived
class C(A):
    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Sorry!"


object_of_c = C()

print(object_of_c.div(10, 20))  # 0.5
print(object_of_c.div(10, 0))  # Sorry!
print(object_of_c.subtration(10, 20))  # -10
print(object_of_c.Addtion(10, 20))  # 30
