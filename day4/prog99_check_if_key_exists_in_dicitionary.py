#Write a program to check if key exists in a dictionary
numbers = {'a': 10, 'b': 20, 'c': 30, 'd': 40}


key = input("Enter the key to search: ")

if key in numbers:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")