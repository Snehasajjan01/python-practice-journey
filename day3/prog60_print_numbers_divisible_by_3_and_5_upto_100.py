#Write program to print the numbers divisible by 3 and 5 upto 100
print('The numbers divisible by 3 and 5 are:')
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end = ",")
