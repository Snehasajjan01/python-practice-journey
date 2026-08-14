#Write a program to check if given string is plaindrome or not
s = input('Enter a string:')
reverse = s[::-1]
if s.lower() == reverse.lower():
    print('The given string is Palindrome')
else:
    print('The given String is not Palindrome')