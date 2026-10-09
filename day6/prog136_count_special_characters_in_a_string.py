#Write python program to count special characters in a string
count = 0 
string = input('Enter a string:')
for char in string:
    if not char.isalnum() and not char.isspace():
        count += 1
print("Number of special characters:",count)