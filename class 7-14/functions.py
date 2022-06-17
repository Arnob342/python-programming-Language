# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# Don't repeat yourself - DRY
"""
def functiona_name():
    statement

def function_name(num1, num2):
    statement

"""



def print_Hello_World():
    print("Hello World")

def print_10_Times_Hello_world():
    i = 1
    while i<11:
        print_Hello_World()
        i+=1

# i = 1
# while i < 11:
#     # print("Hello World")  # Repeat 1
#     print_Hello_World()
#     i += 1

# print("Hello World")  # Repeat 2
# print_Hello_World()
print_10_Times_Hello_world()

str = "abcd"
print(str.lower())