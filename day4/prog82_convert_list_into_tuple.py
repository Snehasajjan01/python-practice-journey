#Write program to convert list to tuple
l = list(map(int,input('Enter the elements:').split()))
print(l)
t = tuple(l)
print(t)
print(type(t))
