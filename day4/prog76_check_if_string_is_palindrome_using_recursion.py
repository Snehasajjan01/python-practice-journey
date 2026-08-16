#Write program to check if string is palindrome using recursion
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])


s = input("Enter a string: ")

if palindrome(s):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")