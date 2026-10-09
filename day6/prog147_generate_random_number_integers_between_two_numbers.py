#Write a python program to generate random integers between two numbers
import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = random.randint(num1, num2)

print("Random integer:", result)
