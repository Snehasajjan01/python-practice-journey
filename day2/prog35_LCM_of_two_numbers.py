n1 = int(input('Enter the 1st number:'))
n2 = int(input('Enter the 2nd number:'))
if n1 > n2:
    greater = n1
else:
    greater = n2
while True:
    if greater % n1 == 0 and greater % n2 == 0:
        lcm = greater
        break
    greater += 1
print("LCM of {},{}:{}".format(n1,n2,lcm))