#Write a python program to define a function that checks if string is palindrome
def string_palindrome(s):
    original_string = s
    reverse = s[::-1]
    if original_string.lower() == reverse.lower():
        print('String is Palindrome')
    else:
        print('String is not Palindrome')
s = input('Enter a String:')
string_palindrome(s)
