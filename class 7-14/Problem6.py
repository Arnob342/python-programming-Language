"""
1. num - Input a Integer

input > 20
output>"20 greater than 10" + "20 is Even Number"

input > 9
output>"9 less than 10" + "9 is odd Number"
"""
print("Please, Input the number - ")
num = int(input()) # 10

if num > 10: # Is 5 greater than 10?
    if num % 2 == 0:  # vagses == 0 hole eta even
        print(str(num) + " greater than 10 and " + str(num) + " is Even Number.")

    elif num % 2 != 0:
        print(str(num) + " greater than 10 and " + str(num) + " is Odd Number.")

elif num < 10: # 5 < 10
    if num % 2 == 0:  # vagses == 0 hole eta even
        print(str(num) + " less than 10 and " + str(num) + " is Even Number.")

    elif num % 2 != 0:
        print(str(num) + " less than 10 and " + str(num) + " is Odd Number.")

elif num == 10:
    if num % 2 == 0:  # vagses == 0 hole eta even
        print(str(num) + " equal to 10 and " + str(num) + " is Even Number.")
