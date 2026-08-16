#Write program to define a function that returns the sum of digits of the number
def sum_of_digits(n):
    intial_sum = 0
    while n != 0:
        last_digit = n % 10
        intial_sum = last_digit + intial_sum
        n = n // 10
    return intial_sum
n = int(input('Enter a number:'))
result = sum_of_digits(n)
print('Sum of digits of {} = {}'.format(n,result))