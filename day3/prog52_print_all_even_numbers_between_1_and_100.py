#Write program to print all the even numbers between 1 and 100
print('Even numbers from 1 to 100 are:')
for i in range(1,100):
    if i % 2 == 0:
        print(i,end = ',')