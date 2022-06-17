#solve-1
def solve(nums):
   return sum([i for i in nums if i % 2 == 1])
nums = [5,7,6,4,6,9,3,6,2]
print(solve(nums))
#output 24


"""
siolve_2
"""
NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)

"""
Please enter the Total Number of List Elements: 4
Please enter the Value of 1 Element : 3
Please enter the Value of 2 Element : 5
Please enter the Value of 3 Element : 6
Please enter the Value of 4 Element : 8

The Sum of Even Numbers in this List =   14
The Sum of Odd Numbers in this List =   8
"""