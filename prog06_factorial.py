#Write a program to find the factorial of a number
def factorial_of_n(n):
    fact = 1
    for i in range(1,n + 1):
        fact = fact * i
    print('Factorial =',fact)
    
n = int(input('Enter any number:'))
if n < 0:
    print('Please enter positive number only..')
else:
    factorial_of_n(n)
