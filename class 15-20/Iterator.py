"""
Iterator: Is an Object that contains sequence of value

"""
"""
# List-Declare
my_list = [1, 2, 3]

# Tuple
my_tuple = (1, 2, 3)


# Convert List to Iterable Object
iter_obj = iter(my_list)
print(type(iter_obj))  # list_iterator

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# Convert Tuple to Iterable Object
iter_obj = iter(my_tuple)
print(type(iter_obj))  # tuple_iterator

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

my_str = "ABCD"
iter_ob = iter(my_str)

print(next(iter_ob))
print(next(iter_ob))
print(next(iter_ob))
print(next(iter_ob))
"""

my_list = [1, 2, 3]

"""
-> Loop:

for num in my_list:
    print(num)
"""

# Iterator
iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
