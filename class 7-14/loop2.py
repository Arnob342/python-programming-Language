"""
1,2,3,4,5

Even Number = 2 + 4 = 6
"""

num = 1
sum = 0

while num <= 5:
    print("-------------------------------------->", num)
    print("Num value is ", num)
    if num % 2 == 0:
        print("Before sum (Sum value): ", sum)
        sum += num
        print("After sum (Sum value): ", sum)

    num += 1
    print("After Increment num value - ", num)
    print("--------------------------------------")

print("Sum of Even - ", sum)
