#Write python program to print pascal's triangle
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        value = 1

        for k in range(j):
            value = value * (i - k) // (k + 1)

        print(value, end=" ")

    print()