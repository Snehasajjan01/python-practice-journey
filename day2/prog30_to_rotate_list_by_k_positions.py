#Write program to roatate a list by 'k' positions(right rotation)
#Original:  [1, 2, 3, 4, 5] , k = 2
#Rotated:   [4, 5, 1, 2, 3]
numbers = list(map(int,input('Enter the list elements:').split()))
k = int(input('Enter number of positions for roatation:'))
k = k % len(numbers)
rotated_list = numbers[-k:] + numbers[:-k]
print('Rotated list',rotated_list)