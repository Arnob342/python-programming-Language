"""
-> def
-> yield instead of Return
"""


def normal_list(my_list):
    return my_list


def traverse_list(my_list):
    yield my_list


my_list_2 = [1, 2, 3]

get_Traverse_list_values = traverse_list(my_list_2)
print(type(get_Traverse_list_values))
print(get_Traverse_list_values)
print(next(get_Traverse_list_values))

get_normal_list = normal_list(my_list_2)
print(type(get_normal_list))
