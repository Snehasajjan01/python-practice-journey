#Write program to remove the duplicates from the list
numbers = list(map(int,input('Enter the elements of the list:').split()))
unique_numbers = []
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
print('List after removing dup;icates',unique_numbers)
