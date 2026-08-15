# Write program to copy contents from one file to another
source_file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\source.txt", "r")
destination_file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\destination.txt", "w")

content = source_file.read()

destination_file.write(content)

source_file.close()
destination_file.close()

print("Content copied successfully.")