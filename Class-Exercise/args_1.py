def print_args_string(*strs):
    print(type(strs))
    for str in strs:
        print(str)


print_args_string("Hello", "World!") # -> ("Hello", "World!")
print_args_string("Hello", "World!", "Python", True, 10, 1.5)
