#Write a python program to count the number of words in a sentence
count = 0
s = input('Enter a sentence:').split()
for word in s:
        count += 1
print('number of words in a sentence are:',count)