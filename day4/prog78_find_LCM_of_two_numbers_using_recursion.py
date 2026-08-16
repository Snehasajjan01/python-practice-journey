#Write program to find the LCM of two numbers using recursion
def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


def lcm(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0

    return abs(n1 * n2) // gcd(abs(n1), abs(n2))


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = lcm(n1, n2)

print("LCM of {}, {} = {}".format(n1, n2, result))