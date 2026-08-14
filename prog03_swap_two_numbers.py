#Write a program to swap two numbers
print('Before swapping first number and second number')
print('-----------------------------------------------')
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
temp = a
a = b
b = temp
print('After swapping first number and second number')
print('-----------------------------------------')
print('The first number is',a)
print('The second number is',b)