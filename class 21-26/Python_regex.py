import re

"""
1. findall
2. search 
3. split 
4. sub 
"""
text = "eshikhon Python Class 24"
"""

getAll24 = re.findall("Class", text)
print(getAll24)

search_char = re.search("Class", text)

print(search_char)

# ['eshikhon', 'Python', 'Class', '24']

split_text = re.split("Python", text)
print(split_text)

sub_text = re.sub("Python", "JavaScript", text)
print(sub_text)
"""
text_a_b = re.findall("[s-t]", text)

print(text_a_b)