# Write program to check if string is palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


string = input("Enter a string: ")

if is_palindrome(string):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")