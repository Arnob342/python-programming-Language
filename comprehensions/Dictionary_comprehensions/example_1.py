# Old
"""
1[Key]:1[Value]
2:8 - Even
3:27
"""
input_list = [1, 2, 3]
output_list = {}

# Old
"""
for num in input_list:
    output_list[num] = num ** 3
"""

# New
output_list = {num: num ** 3 for num in input_list if num % 2 == 0}
print(output_list)

# New
output_list = {num: num ** 3 for num in input_list}
print(output_list)  # {1: 1, 2: 8, 3: 27}
