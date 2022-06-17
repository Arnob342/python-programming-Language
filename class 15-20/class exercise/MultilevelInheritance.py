"""
A->B->C
"""


class A:
    def subtration(self, num1, num2):
        return num1 - num2

    def Addtion(self, num1, num2):
        return num1 + num2


# Child/Derived
class B(A):
    def multi(self, num1, num2):
        return num1 * num2


class C(B):
    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Sorry!"


object_of_c_class = C()
print(object_of_c_class.multi(10, 10)) # B Class
print(object_of_c_class.subtration(10,20)) # A Class
print(object_of_c_class.div(10,20)) # C Class