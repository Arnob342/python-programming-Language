# Function as a Parameter

def textToUpperCase(text):
    return text.upper()


def textToUpperCaseToLowerCase(myFunc, text):
    getText = myFunc(text) # HELLO
    print(getText.lower())


#print(textToUpperCase("hello"))

textToUpperCaseToLowerCase(textToUpperCase, "Hello World")