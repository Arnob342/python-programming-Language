# Given an integer array nums of length n
n = int(input())  # length

# you want to create an array ans of length 2n
nums = []  # 2 * 5 = 10

"""
n = 4 
nums = [0->1,1->2,2->3,3->4]
nums[i] = 
ans = [Nums-> 0->1,1->2,2->3,3->4, || Nums-> ans[0 + 4]4->1, 5->2, 6->3, 7->4]
    = [1,2,3,4,1,2,3,4]
    
0+4=4
1+4=5
"""
"""
Step - 0. 
n = 3
nums = [1,2,3]
ans = [x, x, x, x, x, x] = nums + nums 

-------------------------
ans - List -> nums[Index 0-2] + nums [Index 3-5] 

Step - 1. ans[i] == nums[i]

ans[0] = nums[0] = 1
ans[1] = nums[1] = 2
ans[2] = nums[2] = 3
----------------------------
Step - 2. ans[i + n] == nums[i] 

ans[0+3]->[3] = nums[0] = 1
ans[1+3]->[4] = nums[1] = 2
ans[2+3]->[5] = nums[2] = 3
-----------------------------
ans = [1,2,3,1,2,3]
"""
# Step - 0
index = 0
while index != n:
    num = int(input())
    nums.append(num)
    index += 1
print(nums)

# step - 1

index = 0
ans = []
while index != n:
    ans.append(nums[index])
    index += 1

# Step - 2

for index in range(len(ans)):
    ans.append(nums[index])

# Output
print(ans)
