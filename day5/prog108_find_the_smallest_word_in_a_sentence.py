#Write a Python program to find the smallest word in a sentence
s = input('Enter a sentence:').split()
smallest_word = s[0]
for word in s:
    if len(word) < len(smallest_word):
        smallest_word = word
print("Smallest word in a setence",smallest_word)