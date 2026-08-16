#Write program to count frequency of characters of a string using dictionary
string = input('Enter a string:')
frequency = {}

for character in string:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1
print('Character frequency',frequency)