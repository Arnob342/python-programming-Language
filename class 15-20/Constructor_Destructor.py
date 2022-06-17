class Calculator:
    def __del__(self):
        print("Destructor Calling")

    def __init__(self):
        print("Constructor Calling")

    def getSum(self, num1, num2):
        return num1 + num2

    def getSub(self, num1, num2):
        return num1 - num2


ob = Calculator()
print(ob.getSum(10, 20))
print(ob.getSub(10, 20))
