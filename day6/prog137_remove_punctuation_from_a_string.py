#Write a Python program to remove punctuation from a string
import string
text = input('Enter String that contains punctuation:')
result = " "
for char in text:
    if char not in string.punctuation:
        result += char
print('String without punctuation:',result)