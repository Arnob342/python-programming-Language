# Scenario - 1 [ OLD School]

#
# sum1 = num1 + num2
#
# sum2 = sum1 + num2
#
# print(sum1)
# print(sum2)


# Scenario - 2 [Digital School]

def sum_two_nums(a=10, b=20):
    # sum = a + b
    # return sum
    print(a + b)  # 30


def sum_three_nums(a=10, b=20, c=20):
    return a + b + c  # 50


"""
def fol_dokandar(usertaka, recType):
    return food
    
customer = fol_dokandar(20, amerJuiceden) # food
"""

num1 = int(input())  # 20
num2 = int(input())  # 30

sum_two_nums(num1, num2)  # 50

sum_three_nums = sum_three_nums(num1, num2, 20)  # 50
sum = 20 + sum_three_nums + sum_two_nums(num1, num2)

print(sum)

print(sum_three_nums)  # print sum_three_nums
# print(sum1) # 50

# sum2 = sum_two_nums(sum1, num2) # 50 + 30 = 80
# print(sum2)
