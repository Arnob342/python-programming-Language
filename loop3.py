"""
1,2,3,4,5

Even Number = 1 + 3 + 5 = 9
"""

num = 1
sum = 0

while num <= 100:
    print("-------------------------------------->", num)
    print("Num value is ", num)
    if num % 2 == 1:
        print("Before sum (Sum value): ", sum)
        sum += num
        print("After sum (Sum value): ", sum)

    num += 1
    print("After Increment num value - ", num)
    print("--------------------------------------")

'''
[lINE] 10 - 11 - 12 - 13 - 14 - 15 - 20
10 - 20
10 - 20
10 - 20
10 - 20
10 - fALSE 
'''

print("Sum of Even - ", sum)
print("num valuse is - ", num)