#Write python program to check if character is a special symbol
char = input('Enter a character:')
if not char.isdigit() and not char.isalpha():
    print('Character is a special symbol')
else:
    print('Character is not a special symbol')