"""char_lst = ["A", "B", "C", "D"]

enumerate_char_lst = enumerate(char_lst)
print(type(enumerate_char_lst))

print(list(enumerate_char_lst))

char_lst_2 = ["A", "B", "C", "D"]

enumerate_char_lst_2 = enumerate(char_lst_2, 100)
print(type(enumerate_char_lst_2))

print(list(enumerate_char_lst_2))"""

lst3 = [1, 2, 3, 4]

for element in enumerate(lst3):
    print(element)

result = 0
for element in enumerate(lst3, 100):
    print(type(element))
    result += element

print(result)
