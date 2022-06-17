# Base/Parent Class
class MyCalculator:
    def subtration(self, num1, num2):
        return num1 - num2

    def Addtion(self, num1, num2):
        return num1 + num2


# Child/Derived
class inheritMyCalculator(MyCalculator):
    def multi(self, num1, num2):
        return num1 * num2


obj = inheritMyCalculator()

num1 = int(input())  # 10
num2 = int(input())  # 20

print(obj.Addtion(num1, num2))

num3 = int(input())  # 20
num4 = int(input())  # 10

print(obj.subtration(num3, num4))

print(obj.multi(num1, num2))
