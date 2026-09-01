#Write python program to iterate over a list using 'for' loop
numbers = list(map(int,input('Enter the list of numbers:').split()))
for i in range(len(numbers)):
    print(numbers[i])
