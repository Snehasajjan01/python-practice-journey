# Write program to find the sum of natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)


n = int(input("Enter a number: "))

result = sum_natural(n)

print("Sum of first {} natural numbers = {}".format(n, result))