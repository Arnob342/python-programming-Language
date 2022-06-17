#[3] Write a Python program to find the largest of three numbers.
print("enter three value: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    print("the number is biggest among of the three")
elif num2 > num1 and num2 > num3:
    print("the 2nd number is biggest among off the three")
elif num2 > num1 and num3 > num3:
    print("the 3rd number is biggest among off the three")