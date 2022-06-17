class Calculator:
    def add(self, num1, num2, num3):
        return num1 + num2 + num3


class Calculator2(Calculator):
    def add(self, num1, num2, num3, num4, num5):
        return num1 + num2 + num3 + num4 + num5


obj = Calculator2()
print(obj.add(1, 2, 3, 4, 5))
