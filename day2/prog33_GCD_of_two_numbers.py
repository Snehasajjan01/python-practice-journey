#Write program to find the GCD of two numbers
n1 = int(input('Enter 1st number:'))
n2 = int(input('Enter 2nd number'))
gcd = 1
for i in range(1, min(n1,n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print('GCD of {},{}:{}'.format (n1,n2,gcd))
