#Write a program to find the common elements between two lists
number0 = list(map(int,input('Enter a first list elements:').split()))
number1 = list(map(int,input('Enter a second list elements:').split()))
common_elements = []
for i in number0:
    if i in number1:
        common_elements.append(i)
print('Common elements of the lists are:',common_elements)