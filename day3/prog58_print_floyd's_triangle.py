#Write program to print floyd's triangle
#Floyd's Triangle is a right-angled triangle where consecutive numbers are printed row by row.
n = int(input("Enter the number of rows: "))

number = 1

for i in range(1, n + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()