#Write program to the sum of elements of the list
numbers = list(map(int,input('Enter the list elements:').split()))
sum_list = 0
for i in range(len(numbers)):
    sum_list += numbers[i]
print('Sum of list elements:',sum_list)