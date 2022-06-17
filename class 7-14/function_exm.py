def sum_two_nums(a, b):
    return a + b # 30


def print_two_nums_sum(num1, num2):
    print(num1 + num2)


def return_hello_world():
    return "Hello World"


def print_Hello_world():
    print("Hello World")


num1 = 10
num2 = 20

sum1 = sum_two_nums(num1, num2)  # 10 + 20 = 30

# sum2 = sum1 + print_two_nums_sum(sum1, num2) # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

print("Sum1", sum1)
print_two_nums_sum(sum1, num2)

print(return_hello_world())

print_Hello_world()