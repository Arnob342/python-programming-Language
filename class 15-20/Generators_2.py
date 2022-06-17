def generator_function():
    num = 3
    yield num

    num = num + 10
    yield num

my_gen = generator_function()

"""
print(next(my_gen))
print(next(my_gen))
"""
"""
for gen in my_gen:
    print(gen)
"""
