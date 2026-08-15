#Write program to check if a number is perfect number
#Perfect number-it is a positive number which is sum of it's divisors except itself
#ex-6=1+2+3
n = int(input('Enter a number:'))
sum_of_divisors = 0
for i in range(1,n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print('The given number is perfect number')
else:
    print('The given number is not perfect number')