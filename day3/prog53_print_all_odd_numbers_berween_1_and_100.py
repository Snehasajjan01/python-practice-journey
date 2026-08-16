#Write program to print all the odd numbers from 1 to 100
print('Odd numbers between 1 to 100 are:')
for i in range(1,100):
    if i % 2 == 1:
        print(i,end=',')
