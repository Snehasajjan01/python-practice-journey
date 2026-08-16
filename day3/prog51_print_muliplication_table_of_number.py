#Write a program to print the multiplication of the table
n = int(input('Enter a number:'))

for i in range(1,11):
    multiplication_of_table = n * i
    print('{} * {} = {}'.format(n,i,multiplication_of_table))