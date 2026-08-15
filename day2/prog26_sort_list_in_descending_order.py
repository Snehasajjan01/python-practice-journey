#Write program to sort list in descending order
numbers = list(map(int,input('Enter the list elements:').split()))
numbers.sort(reverse =  True)
print('List in decending order:',numbers)