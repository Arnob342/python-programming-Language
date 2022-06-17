"""
2 + 3 + 5 + ... + N[1-100]

---------------------
n = 99

2 + 3 + 5 + 7

sum = 17
-----------------------

"""


# 1 and nums % 0 = Prime
# function - 
def isPrimeNumber(num):
    # Return True - Prime / False - Not Prime
    count = 0
    for n in range(1, num + 1):
        if num % n == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False


num = input()  # n
sum = 0

for i in range(2, num + 1):
    result = isPrimeNumber(i)  # 2/3/4/5/6/7
    if result is True:
        sum += i

print(sum)
