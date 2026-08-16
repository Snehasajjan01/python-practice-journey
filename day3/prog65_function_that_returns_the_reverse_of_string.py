#Write program that defines the function to return the reverse of the string
def reverse_string(s):
    reverse = s[::-1]
    print('Reverse of {} = {}'.format(s,reverse))
s = input('Enter a string:')
reverse_string(s)
