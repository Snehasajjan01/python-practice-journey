#Write a program to remove all spaces from the string
word = input('Enter a String:')
for i in word:
    spaces_removed = word.replace(" ","")
print('String after removing spaces',spaces_removed)