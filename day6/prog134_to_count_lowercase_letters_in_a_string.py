#Write python program to count lowercase letters in a string
string = input('Enter the string:')
count = 0
for char in string:
    if char.islower():
        count += 1
print('Number of lowercase letters in a string are',count)