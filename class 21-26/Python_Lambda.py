"""
-> Anonymous Function
-> n args
-> [Syntax] lambda arguments : expression
"""
"""
-> Lambda function vs def function ?
"""
## Normal def
"""
def add100WithN(n):
    return n + 100

print(add100WithN(10))
"""
# Lambda Function

# Arguments - 1
"""
add100WithN_Lambda = lambda n : n + 100

num = int(input())
print(add100WithN_Lambda(num))
"""
# Arguments - 2
"""
sumTwoNums = lambda num1, num2 : num1 + num2

num1 = int(input())
num2 = int(input())

print(sumTwoNums(num1, num2))
"""
# Arguments - 3
"""
sumThreeNums = lambda num1, num2, num3 : num1 + num2 + num3

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(sumThreeNums(num1, num2, num3))
"""
# Arguments - n args
"""
nArgsLambda = lambda *args: print(args)

nArgsLambda(1,2,3)
"""
# sum  n arguments
"""
nArgsLambda = lambda *args: sum(args)

print(nArgsLambda(1,2,3))
"""
# sum -> 1 to N [1+2+3+...+N]
"""
N = int(input())

sum_one_To_N = lambda N : sum(range(1, N+1))

print(sum_one_To_N(N))
"""
# Sum  all list data
# [1,2,3,4] = 10
"""
lst_1 = [1, 2, 3, 4] # 10
lst_2 = [1, 2, 3, 4, 5, 6, 7] # 28


sum_the_lst = (lambda *num : sum(num))

print(sum_the_lst(*lst_1))
print(sum_the_lst(*lst_2))
"""

# lambda function
"""
get_max_value_between_two_nums = lambda num1, num2 : num1 if(num1>num2) else num2
get_min_value_between_two_nums = lambda num1, num2 : num1 if(num1<num2) else num2

print(get_max_value_between_two_nums(2, 5))
print(get_min_value_between_two_nums(2, 5))
"""
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_num_lst = list(filter(lambda num : (num % 2 == 0), lst))
print(even_num_lst)

odd_num_lst = list(filter(lambda num : (num % 2 == 1), lst))
print(odd_num_lst)
"""
"""
ages = [10, 20, 45, 80, 90, 100]

get_ages_more_than_80 = list(filter(lambda age : age>80, ages))
print(get_ages_more_than_80)
"""

mens = ["Mr Joy", "Nazmul Hasan", "Mostafa Kamal"]

# ['MR JOY', 'NAZMUL HASAN', 'MOSTAFA KAMAL']
"""
upper_mens = []

def uppered_mens(mens):
    for men in mens:
        upper_mens.append(str.upper(men))

    print(upper_mens)


uppered_mens(mens)

upper_mens_comprehension_version = [str.upper(men) for men in mens]
print(upper_mens_comprehension_version)

upper_mens_lambda_version = list(map(lambda men : str.upper(men), mens))
print(upper_mens_lambda_version)
"""
"""
lst = [1, 2, 3, 4, 5]
# [10+1, 10+2, 10+3, 10+4]

# Solution - 1
lst_add_10 = list(map(lambda num : num + 10, lst))


print(lst_add_10)

def func(num):
    return num + 10
"""

lst = [1, 2, 3, 4, 5]

sum_lst = 0

for num in lst:
    sum_lst += num

print(sum_lst)

from functools import reduce

sum_lst_v2 = reduce(lambda x, y: x + y, lst)

# [1,2] = [3,3] = [6,4] = [10, 5] = [15]

print(sum_lst_v2)
