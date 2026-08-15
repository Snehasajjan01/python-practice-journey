#Write program to find the longest word in file
# Write program to find the longest word in a file

file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\source.txt", "r")

content = file.read()
words = content.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)

file.close()