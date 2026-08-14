#Write a program to find the length of the string without using length function
word = input('Enter a String:')
count = 0
for i in word:
    count += 1
print('Length of the String:',count)