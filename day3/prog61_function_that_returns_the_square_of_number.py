#Write python program to define a function that return the square of a number
def square_of_number(n):
    square = n * n
    print('Square of {} is {}'.format(n,square))
n = int(input('Enter a number:'))
square_of_number(n)