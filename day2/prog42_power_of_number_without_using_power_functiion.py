#Write program to calaculate power of a number without using power function
n = int(input('Enter a number:'))
power = int(input('Enter power value:'))
result = 1
for i in range(power):
    result = n * result
print('Value of {} ^ {}:{}'.format(n,power,result))
