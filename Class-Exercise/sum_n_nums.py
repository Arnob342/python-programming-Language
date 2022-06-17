"""
*args - Non keywords Arguments
"""


def sum_n_nums(*nums):  # *nums -> (1, 1)
    sum = 0
    for num in nums:  # nums = (1,1)
        sum += num
        # Step - 1 => sum = sum + num = 0 + 1 = 1
        # Step - 2 => sum = sum + num = 1 + 1 = 2
    return sum  # 2


sum = sum_n_nums(1, 1)
# print(sum)  # Case 1
# print(sum_n_nums(1, 2, 3, 4))
# print(sum_n_nums(1, 2, 3, 4, 5, 6, 7))

if sum % 2 == 1:
    print("Print your are lucky")
else:
    print("Sorry")

