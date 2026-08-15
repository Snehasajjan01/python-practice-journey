#Write a program to count the vowels and consonants of a string
word = input('Enter a String:')
vowels = 0
consonants = 0
n = len(word)
for i in range(n):
    if word[i] == 'a' or word[i] == 'i' or word[i] == 'o' or word[i] =='e' or word[i] == 'u':
        vowels += 1
    else:
        consonants += 1
print('The number of consonants in the given word are:',consonants)
print('The number of vowels in the given word are:',vowels)