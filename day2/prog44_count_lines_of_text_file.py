#Write program to count number of lines in a text file
# Write a program to count lines in a text file

file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\sample.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()