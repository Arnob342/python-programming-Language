# File Open

# Operation - 1 : Open

"""
open(fileName, AccessMode, Buffering)
"""

# AccessMode:

"""
r -> Read
w -> write
----------
rb
r+
rb+
w
wb
w+
wb+
a
ab
a+
ab+
"""
# Example - 01

# Code version - 1
"""
doc_file = open("documents.txt", "r")
content = doc_file.read()
print(content)
# Output: Programming is very versatile; you have to see the big picture.
doc_file.close()
"""

# Code version - 2
try:
    doc_file = open("documents.txt", "r")
    content = doc_file.read()
    print(content)
except:
    print("Something went wrong.")
finally:
    doc_file.close()
