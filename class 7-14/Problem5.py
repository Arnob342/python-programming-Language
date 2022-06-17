"""
Vowel - AEIOU/aeiou
Consonant - !Vowel
"""

print("Please, Input the Character - ")
character = input()

if character in "AEIOUaeiou":
    print("Vowel")
elif character not in "AEIOUaeiou":
    print("Consonant")
