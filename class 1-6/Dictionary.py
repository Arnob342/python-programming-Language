dictionary_Declaration = {}
print(type(dictionary_Declaration))

# Key:value


dict2 = {
    0: 10,
    1: 20,
    2: 30
}

# dict3 = {'key': 'value', 'key2': 'value2'}

# Dictionary Declare

# dict5 = dict() # Empty Dict Declare
#
# key = input() # User Input - Key Data
# value = input() # User Input - Key value
#
# dict5 = {
#     key: value
# }
# print(dict5)

dict1 = {
    'name': 'Arnob Reduan',
    'email': 'arnobreduan679@gmail.com',
    'phone': '01407749342',
    'deletekey': ' I will delete you soon :P?'
}

dict4 = {
    "hometown": "sherpur"
}
# print(dict1)

# Empty Dictionary Declare

# dict4 = dict()

# dict4 = {1: 10}
# print(dict4)

# Access Item - Dictionary
# print(dict1['name'])
#
# Update Item - Dictionary
# dict1['name'] = 'Mahmud Hasan'
# print(dict1)
#
# name_and_hometown = dict1['name'] + " and " + dict4['hometown']
# print(name_and_hometown)

# print(dict1['name'] + " " + dict4['hometown'])
# print(dict4)
# Print Two dictionary
# print(dict1, dict4, dict2)  # No Update / Add. Just print dictionary data

# Combine two dictionary into one | As like list - append
# dict1.update(dict4, dict2)
# print(dict1)

# print(dict1)
# Delete key from dictionary
# del dict1['deletekey']
#del dictionary_Name['Key_Name']
# print(dict1)

#Clear dictionary
# dict1.clear()
# print(dict1)

# dict1.update(dict2, dict4) # TypeError: update expected at most 1 argument, got 2

# dict1.update(dict2)
# dict1.update(dict4)
# print(dict1)

print('name' in dict1) # 'name' ki dict1 a ache ?

print(dict1.keys())
print(dict1.values())

print(dict1['name'])
print(dict1.get("name"))

