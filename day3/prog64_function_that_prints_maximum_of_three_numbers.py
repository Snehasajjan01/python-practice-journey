#Write program that define function to retrn maximum of three elements
def maximum_of_three(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print('{} is greater than {} and {}'.format(n1,n2,n3))
    elif n2 > n1 and n2 > n3:
        print('{} is greater than {} and {}'.format(n2,n1,n3))
    else:
        print('{} is greater than {} and {}'.format(n3,n1,n2))
n1 = int(input('Enter 1st number:'))
n2 = int(input('Enter 2nd number:'))
n3 = int(input('Enter 3rd number'))
maximum_of_three(n1,n2,n3)