#Write program to prin the sum of the tuple elements
numbers = tuple(map(int,input('Enter the tuple elements:').split()))
elements_sum = 0
for i in range(len(numbers)):
    elements_sum = numbers[i] + elements_sum
print('Sum of tuple elements:',elements_sum)