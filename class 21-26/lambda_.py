"""
-> Anonymous
-> n args
#->[syntx] lambda arguments : expression
"""
"""
Lambda fungtion vs def fungtion
"""
# Normal def fungtion

def add100withN(n):
    return n + 100
print(add100withN(10))
#lambda fungtion
add100withN_lambda = lambda n : n + 100
print(add100withN_lambda(10))

num = int(input())
print(add100withN_lambda(num))

# argumenta -2


num1 = int(input("Enter"))
num2 = int(input("Enter"))
sumTwo = lambda num1, num2 : num1 + num2

print(sumTwo(num1, num2))
print(type(num2))