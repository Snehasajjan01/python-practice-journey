#Write python program to define the function that calculates factorialusing recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input('Enter a number:'))
result = factorial(n)
print('{}! = {}'.format(n,result))

