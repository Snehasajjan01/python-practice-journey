# Write program to remove blank lines from a text file

file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\destination.txt", "r")

lines = file.readlines()

file.close()

file = open("sample.txt", "w")

for line in lines:
    if line.strip() != "":
        file.write(line)

file.close()

print("Blank lines removed successfully.")