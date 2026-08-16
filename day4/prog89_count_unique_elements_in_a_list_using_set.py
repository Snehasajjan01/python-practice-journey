#Write program to count unique elements in the list using set
list = list(map(int,input('Enter the list elements:').split()))
unique_elements = set(list)
print('Unique_numbers =',unique_elements)
print("Number of unique_elements:",len(unique_elements))