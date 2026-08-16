#Write program to find the key with the maximum value in a dictionary
numbers = {'a':1,
           'b':3,
           'c':8,
           'd':19,
           'e':56}
max_value = 0
max_key =''
for key,value in numbers.items():
    if value > max_value:
        max_value = value
        max_key = key
print('Key with Maximum value:',max_value)
print('Maximum Value: ',max_value)
