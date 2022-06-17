"""
A -> D
B -> D
C -> D
"""


class A:
    def add(self, num1, num2):
        return num1 + num2


class B:
    def sub(self, num1, num2):
        return num1 - num2


class C(A, B):
    def multi(self, num1, num2):
        return num1 * num2

