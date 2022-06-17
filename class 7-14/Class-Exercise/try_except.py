num1 = "A"
num2 = 20
"""
if num1 != 0:
    print(num2/num1)
else:
    print("Not divisible by 0")

print(10) # ctrl+shift+Arrow
"""

try:  # Try -
    print(num2 / num1)  # ABC
except ValueError:
    print("Value Error Exception")
except ZeroDivisionError: # 2/0
    print("ZeroDivisionError")
except Exception as exception:
    print("Unknown Exception")
finally:
    print("Always Execute")

print(10)
