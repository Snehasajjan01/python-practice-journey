#Write a program to count the occurrence of a substring
string = input('Enter a string:')
substring = input('Enter a substring:')
count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        count += 1
print('Total number of substring',count)
