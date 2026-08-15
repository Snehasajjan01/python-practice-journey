#Write program to write a textfile
file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\sample.txt", "w")

file.write("Hello, I am learning Python.")
file.write("\nThis is my first text file.")
file.write("\nI enjoy learning process.")

file.close()

print("Data written successfully.")