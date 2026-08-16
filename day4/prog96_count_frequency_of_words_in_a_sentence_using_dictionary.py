#Write program to count frequency of words in a sentence using dictionary
sentence = input('Enter a sentence:')
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print('Word frequency:',frequency)