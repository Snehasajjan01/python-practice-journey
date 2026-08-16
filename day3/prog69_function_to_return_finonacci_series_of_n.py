#Write program to define function that return the fibonacci series of n
def fibonacci(n):
    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


n = int(input("Enter the number: "))

result = fibonacci(n)

print("Fibonacci series:", result)