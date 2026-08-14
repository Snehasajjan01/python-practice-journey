#Write a program to find the largest of three numbers
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a > b and a > c:
    print(a,'is the largest value')
elif b > a and b > c:
    print(b,'is the largest value')
else:
    print(c,'is the largest value')