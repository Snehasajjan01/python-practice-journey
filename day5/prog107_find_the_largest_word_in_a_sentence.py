#Write Python Program to find the largest word in a sentence
s = input('Enter a sentence:').split()
largest_word = " "
for word in s:
    if len(word) > len(largest_word):
        largest_word = word
print("Largest word =" , largest_word)
