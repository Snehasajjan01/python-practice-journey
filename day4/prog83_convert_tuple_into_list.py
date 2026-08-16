#Write program to convert tuple to list
t = tuple(map(int,input('Enter the elements:').split()))
print(t)
l = list(t)
print(l)
print(type(l))