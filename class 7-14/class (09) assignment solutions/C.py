nums = [1, 2]
"""
[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]

[1, 3, 6, 10]
"""
"""
locate index = 4
current index = 0 - 3 
[0 -> 1, 1 -> 2, 2 -> 3, 3 -> 4]

[1, 1+2, 1+2+3, 1+2+3+4]
"""
print(nums)
out_list = []
point_index = 0  # Current Locate Index
for num in nums:  # [ 1,2,3,4]
    print("------------------Start---------------------")
    # 4 -> Index - 3 -> Point Index
    index = 0  # Start Index of List
    sum = num  # Current/Point Index value
    print("Current/Point Index - ", point_index)
    # Current - 3
    # [ Index -> 0, 1, 2]
    while index < point_index:
        print("nums[Index] - nums[", index, "]")
        sum += nums[index]
        print("Sum - ", sum)
        index += 1

    print("Total Sum - ", sum)
    out_list.append(sum)
    point_index += 1
    print("------------------End---------------------")
print(out_list)
