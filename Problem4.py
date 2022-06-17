"""
1. Take a Character(String) Input
2. Upper Case/Lower case

Input > A
Output > Upper Case
Input > a
Output > Lower Case
"""
print("Please, Input the Character - ")
character = input()
"""
a - z = lower case 
A - Z = Upper Case 
"""
if character >= "A" and character <= "Z": # D
    print("Upper Case!")
elif character >= "a" and character <= "z":
    print("Lower Case!")
else:
    print("Nothing!")
