"""Algorithm Approach - 1"""

import math
x = int(input("Enter a number: "))
square_root_value_without_decimal_point = int(math.sqrt(x))
print(square_root_value_without_decimal_point)

"""Algorithm Approach - 2"""
square_root_value_without_decimal_point = int(x ** (1 / 2))
print(square_root_value_without_decimal_point)
