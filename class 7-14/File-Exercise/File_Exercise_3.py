my_file = open("test.txt", "r")

content = my_file.read(5)
print(content) # Line

# content = my_file.read()
# print(content)
# - 1: Programming is very versatile; you have to see the big picture.
# Line - 2: Programming is very versatile; you have to see the big picture.

content = my_file.tell()
print(content)

"""
0 - Start
1 - Current
2 - End
"""
content = my_file.seek(0, 0)
content = my_file.tell()
print(content)

content = my_file.read()
print(content)

content = my_file.readline()
print(content)

my_file.close()
