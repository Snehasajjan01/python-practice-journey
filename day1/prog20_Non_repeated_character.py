#Write program to print the first non repeated character
string = input('Enter a String:')
for i in string:
    if string.count(i) == 1:
        print('First non repated character:',i)
        break
