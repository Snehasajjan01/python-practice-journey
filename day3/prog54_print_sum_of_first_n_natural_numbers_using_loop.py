#Write program to sum of first n naatural numbers using loop
initial_sum = 0
n = int(input('Enter a number:'))
for i in range(n):
    initial_sum = initial_sum + i
print('Sum of first {} natural numbers = {}'.format(n,initial_sum))
