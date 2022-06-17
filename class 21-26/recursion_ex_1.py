def printNTo1(num):  # num = 3
    # 3 2 1
    while num > 0:  # 3 | 2 |  1 | 0 [False]
        print(num)  # 3 | 2 | 1
        num -= 1  # 2 | 1 | 0


def printNTo1_recursion(num): # 3 | 2 | 1
    # 1. Terminate Case ->
    # 2. Recursion Case ->
    print(num) # 3 | 2 | 1
    num = num - 1  # 2 | 1 | 0
    if num > 0:
        printNTo1_recursion(num) # 2 | 1


printNTo1(3)
print("------------------")
printNTo1_recursion(3)


