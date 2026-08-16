#Write program to check if set is subset of another set
s1 = set(map(int,input('Enter the set 1 elements:').split()))
s2 = set(map(int,input('Enter the set 2 elements:').split()))
if s1.issubset(s2):
    print('First set is subset of second set')
else:
    print('First set is not subset of second set')