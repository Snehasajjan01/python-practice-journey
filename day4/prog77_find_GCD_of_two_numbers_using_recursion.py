#Write program to find the GCD of two numbers using recursion
def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = gcd(n1, n2)

print("GCD of {}, {} = {}".format(n1, n2, result))