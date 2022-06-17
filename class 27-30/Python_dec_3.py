"""
num1, num2 = 5, 6

1,2 = 1/2
2,1 = 1/2

division = min/max = 5/6

"""
#
# def division(num1, num2):
#     if(num1 > num2):
#         return num1/num2
#     else:
#         return num2/num1
#
# print(division(2,1))

#--------------------------------

def div(num1, num2):
    print("DIV Function") # Step - 2
    return num1/num2

def div_decorator_func(func):
    def inner_decorator_func(num1, num2): # 2, 1
        if num1 < num2:
            num1, num2 = num2, num1
        else:
            num1, num2 = num1, num2

        div_result = func(num1, num2)  # div(num1, num2) # Step - 1
        print("After Div Result")
        return div_result # Step - 3
    output = inner_decorator_func
    print("After Inner Decorator func.")
    return output

newDiv = div_decorator_func(div)
print(newDiv(2,1))


