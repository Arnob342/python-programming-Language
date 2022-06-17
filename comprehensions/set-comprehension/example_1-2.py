input_list = [1, 2, 3, 4, 5]

# Old
""""
output_set = set()
for num in input_list:
    if num % 2 == 1:  # Odd Num 
        output_set.add(num)  # Add Odd number into set 
"""

# New
output_set_2 = {num for num in input_list if num % 2 == 1}
print(output_set_2)  # {1, 3, 5}
