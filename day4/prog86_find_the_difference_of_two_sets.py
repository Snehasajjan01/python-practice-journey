#Write program to find the difference of two sets
s1 = set(map(int,input('Enter set 1 elements:').split()))
s2 = set(map(int,input('Enter set 2 elements:').split()))
print('Difference of set 1 and set 2 is',s1 - s2)
print('Difference of set 2 and set 1 is', s2.difference(s1))