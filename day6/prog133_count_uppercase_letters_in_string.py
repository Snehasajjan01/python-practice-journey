#Write python program to count uppercase letters in a string
string = input('Enter a string:')
count = 0
for char in string:
    if char.isupper():
        count += 1
print('Uppercase letters in string are:',count)