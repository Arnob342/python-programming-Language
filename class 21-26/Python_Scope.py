"""
1. Scope
2. Local Scope
3. Global Scope
4. Local Variable
5. Global Variable

"""

result = 10  # Variable - Global Scope


def addTwoNumbers(x, y):
    sum = x + y  # Variable - Local Scope
    sum += result
    global mul # Variable - Global Scope
    mul = sum * result
    print(mul)
    print(sum)


num1 = 10  # Variable - Global Scope
num2 = 20  # Variable - Global Scope
addTwoNumbers(num1, num2)
print(mul)
