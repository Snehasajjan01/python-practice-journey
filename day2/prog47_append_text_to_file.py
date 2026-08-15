#Write a program to append text to a file

file = open(r"C:\Users\Sneha Sajjan\Desktop\GQT\Python programs\day2\source.txt", "a")

text = input("Enter text to append: ")

file.write("\n" + text)

file.close()

print("Text appended successfully.")