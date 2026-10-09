#Write Python Program to check if character is uppercase
string = input("Enter the Sentence:").split()

if string.isupper():
    print('The characters in the string are uppercase')
else:
    print('The characters in the string are not uppercase')