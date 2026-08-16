#Write program to find the union of two sets
s1 = set(map(int,input('Enter 1st set elements:').split()))
s2 = set(map(int,input('Enter 2nd set elements:').split()))
print('s1 | s2 =',s1 | s2)
print('Union of set1 and set2 is', s1.union(s2))