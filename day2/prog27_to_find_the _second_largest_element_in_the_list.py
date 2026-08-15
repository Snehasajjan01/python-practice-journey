#Write program to find the second largest element in the list
numbers = list(map(int,input('Enter the list elements:').split()))
numbers.sort(reverse=True)
print('Second largest element in the list is:',numbers[1])