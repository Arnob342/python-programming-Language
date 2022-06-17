
# Old Version

input_list = [1, 2, 3, 4, 5]
output_list = []

for num in input_list:
    if num % 2 == 0:
        output_list.append(num)

print(output_list) # [2, 4]


# New Code - Comprehensions

input_list = [1, 2, 3, 4, 5]

# With Condition
output_list = [num for num in input_list if num % 2 == 0]
# [ (output_expression) (for num in input_list) (if (condition))]
print(output_list)  # [2, 4]

# Without Condition
output_list_1 = [num for num in input_list]
print(output_list_1)  # [1, 2, 3, 4, 5]
