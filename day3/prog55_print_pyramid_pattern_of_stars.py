#Write python program to print pyramid pattern of stars
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)