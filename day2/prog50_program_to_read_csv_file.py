#Write program to read a CSV file
# Write program to read a CSV file

import csv

file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()