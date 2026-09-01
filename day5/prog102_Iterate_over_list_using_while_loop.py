#Write python program to iterate over list using 'while' loop
numbers = list(map(int,input('Enter the list elements:').split()))
while len(numbers) > 0:
    print(numbers)
    break