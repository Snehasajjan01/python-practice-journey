#Write program to reverse a string using recursion
def reverse_string(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


string = input("Enter a string: ")

result = reverse_string(string)

print("Reversed string:", result)