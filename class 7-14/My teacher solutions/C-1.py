nums = []

total_nums_of_input = int(input("Total number of input: "))

# Input Data into list
while total_nums_of_input > 0:
    num = int(input())
    nums.append(num)
    total_nums_of_input = total_nums_of_input - 1

out_list = []
point_index = 0
for num in nums:
    index = 0
    sum = num
    while index < point_index:
        sum += nums[index]
        index += 1
    out_list.append(sum)
    point_index += 1

print(out_list)
