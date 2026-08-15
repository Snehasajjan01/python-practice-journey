#Write program to read text file
file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\sample.txt", "r")

content = file.read()

print(content)

file.close()