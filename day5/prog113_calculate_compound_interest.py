#Write python program to calculate the compound interest
p = int(input('Enter Prinicipal amount:'))
r = int(input('Enter Rate of Interest:'))
t = int(input('Enter Time Period in terms of years:'))
compound_interest = p * (1 + (r/100))**t
print("Simple interest is",compound_interest)