#Write python program to count digits in a string
string = input('Enter the string:')
count = 0
for char in string:
    if char.isdigit():
        count += 1
print('Total number of digits in a string', count)