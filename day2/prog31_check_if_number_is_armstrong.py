#Write program to check if number is armstrong number
#Armstrong Number:A number where the sum of each digits raised to the number of digits is equal to the original number
#ex:153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
number = int(input('Enter a number:'))
original_number = number
s = 0
n = len(str(number))
while number != 0: 
    last_digit = number % 10
    individul_number = last_digit ** n
    s = s + individul_number
    number = number // 10
if s == original_number:
    print('The given number is ArmStrong')
else:
    print('The given number is not ArmStrong')
