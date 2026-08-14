#Write a program to check if strings are anagram
string1 = input('Enter a string1:')
string2 = input('Enter a string2:')
if sorted(string1) == sorted(string2):
    print('Two strings are anagram')
else:
    print('Given strings are not anagram')