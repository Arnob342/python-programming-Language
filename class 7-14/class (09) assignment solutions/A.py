# import math


# Compute and Return the square root of x.
def squareRootOfX(x):
    # Only the integer part of the result is returned.
    return int(x ** (1 / 2))


# Given a non-negative integer x
x = int(input())

if x >= 0:
    result = squareRootOfX(x)
    print(result)
else:
    print("Number must be non-negative integer.")
