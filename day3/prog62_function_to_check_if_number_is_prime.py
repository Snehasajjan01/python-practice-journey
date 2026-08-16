def prime_number(n):
    if n == 2:
        print('{} is prime number'.format(n))
    if n % 2 == 0:
        print('{} is not prime number'.format(n))
    else:
        print('{} is prime number'.format(n))
n = int(input('Enter a number:'))
prime_number(n)