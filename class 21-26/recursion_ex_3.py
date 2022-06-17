"""

factorial = 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = Result

"""


# Normal Process
def factorial(num):
    result = 1  # 1
    for index in range(1, num + 1):
        result *= index  # 10 * 10 *..........*10*0
    return result


# Abnormal Mode :P [Recursion Mode]
def factorial_recursion(num):
    if num > 0:
        return num * factorial_recursion(num - 1)
    else:
        return 1


print(factorial(7))
print(factorial_recursion(7))
