"""
Input -> 5
[0,1,2,3,4]

output- [0^2, 1^2, 2^2, 3^2, 4^2]
"""

# Old Version
"""
range_limit = int(input())
output_list = []
for num in range(0, range_limit):
    output_list.append(num ** 2)

print(output_list) # [0, 1, 4, 9, 16]
"""
"""
# New Code 
range_limit = int(input())

output_list_2 = [num ** 2 for num in range(0, range_limit)] # range (min,max-1)
print(output_list_2) # [0, 1, 4, 9, 16]
"""


output_list_str = ["A", "B", "C"]
vowels = ["A", "E", "I", "O", "U"]

output_list_str_out = [str for str in output_list_str if str in vowels]
print(output_list_str_out)  # ['A']
