#Write program to count words in a text file
file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\sample.txt", "r")

content = file.read()

words = content.split()

print("Number of words:", len(words))

file.close()