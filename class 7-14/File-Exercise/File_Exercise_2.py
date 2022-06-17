# Code Version - 1
"""
doc_file = open("write_doc.txt", "w")

doc_file.write("Hello World!")
doc_file.close()
"""

# Code version - 2

try:
    doc_file = open("write_doc.txt", "w")
    doc_file.write("I want to.")
except:
    print("File Read Error Occurs...")
finally:
    doc_file.close()
