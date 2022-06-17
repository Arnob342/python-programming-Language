"""
for var in sequence-list/range()/diction/set:
    statements
"""
# list = ["A", "B", "C"]
#
# for list_element in list:
#     print(list_element, end=" ")

# str = "Class-09"
# for ch in str:
#     print(ch, end="\t")
# if ch == "C":
#     print(ch, end="\t")

# Tuple
# tuple_dec = ("A", "C", "D")
#
# for tuple_elem in tuple_dec:
#     print(tuple_elem)
#
# set_dec = {1,2,3,4}
#
# for set_elem in set_dec:
#     print(set_elem)

dictionary = dict()
dictionary['name'] = "ABC"
dictionary["Country"] = "Bangladesh"

dictionary1 = {
    "name": "ABD",
    "Country": "Bangladesh"
}

for key in dictionary1:
    print("-------------")
    print(key) # Key
    print(dictionary1[key]) # Value
    print("-------------")
