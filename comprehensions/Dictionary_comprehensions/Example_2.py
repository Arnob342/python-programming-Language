country = ["Bangladesh", "Germany"]
state = ["Dhaka", "Berlin"]

"""
- Create a dictionary based on two list 
- [Key]:[Value]
- [Country]:[State]
"""
"""
[Bangladesh->Dhaka]
[Germany->Berlin]
"""
# OLD
out_dict = dict()
for (key, value) in zip(country, state):
    out_dict[key] = value
print(out_dict) # {'Bangladesh': 'Dhaka', 'Germany': 'Berlin'}

# New
out_dict_2 = {key:value for (key, value) in zip(country, state)}
print(out_dict_2) # {'Bangladesh': 'Dhaka', 'Germany': 'Berlin'}
