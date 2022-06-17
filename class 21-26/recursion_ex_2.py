# num = 10
# 1 + .. + 10 = SUM

def sum(num):
    total = 0
    for index in range(num + 1):
        total += index
    print(total)


sum(3)


# 1. n > 0
# 2. n == n

def sum_recursion_implementation_1(num):  # 3 | 2
    if num > 0:  # True | True
        return num + sum_recursion_implementation_1(num - 1)  # 0 + 1 = 1 + 2 + 3 = 6
    else:
        return 0


print(sum_recursion_implementation_1(3))


def sum_recursion_implementation_2(num):
    exact_num = num

# // 1 + 2 + 3 + ... + N - Pending

# // N + .. + 3 + 2 + 1 - Already Done

# 1. Section [Complete]
# 2. Sub Section [Complete ]
# 3. Sub Sub Section [Complete]
