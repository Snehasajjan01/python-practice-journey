#Write program to check if element exits in tuple
numbers = tuple(map(int,input('Enter the tuple elements:').split()))
element = int(input('Enter the element to search:'))
if element in numbers:
    print('Element exists in the tuple')
else:
    print("Element doesn't exists in the tuple")