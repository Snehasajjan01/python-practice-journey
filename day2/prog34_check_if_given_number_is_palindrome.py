#Write program to check if given number is Palindrome
n = int(input('Enter a number:'))
original_number = n
rev = 0
while n != 0:
    last_digit= n % 10
    rev = rev * 10 + last_digit
    n = n // 10 
print('Reverse of a number:',rev)
if rev == original_number:
    print('The given number is Palindrome')
else:
    print('The given number is not Palindrome')
