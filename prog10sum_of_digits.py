#Write a program to print the sum of digits of the given number
n = int(input('Enter a number:'))
sum_of_digits = 0
while n != 0:
    last_digit = n % 10
    sum_of_digits = sum_of_digits + last_digit
    n = n // 10
    
print('Sum of Digits =',sum_of_digits)
