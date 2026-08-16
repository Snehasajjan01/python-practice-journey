#Write python program to define the funcyion that returns the power of number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)

print("{} raised to the power {} = {}".format(base, exponent, result))