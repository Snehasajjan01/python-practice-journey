#Write program to find the sum of natural numbers upto n
n = int(input('Enter a number:'))
intial_sum = 0
for i in range(1,n + 1):
    intial_sum += i
print('Sum of natural numbers upto {}:{}'.format(n,intial_sum))