# range

"""
1. range(stop)
2. range(start, stop, step)
"""

# Example - 1
# Output - 0 1 2 3 4
# for num_in_range in range(5):  # [0,1,2,3,4]
#     print(num_in_range)

# Example - 2
# for i in range(2, 5):  # [0,1,2,3,4]
#     if i % 2 == 0:
#         print(i)

# print()
#
#
# Example - 3
# for i in range(0, 10, 3): # (Start, End, Increment)
#     print(i)
# print()
#
#
# Example - 4
# start = int(input())
# for i in range(start, -10, -2):  # [10,2,-2] # 10+(-2)=10-2=8 | 8+(-2)=6 | 4
#     print(i, end=",")

for char in range(ord("@"), ord("A") + 1):  # Integer
    print((chr(char)))
# 10 8 6 4
# print()
#
