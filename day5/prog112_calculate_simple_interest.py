#Write python program to calculate the simple interest
p = int(input('Enter Prinicipal amount:'))
r = int(input('Enter rate of interest:'))
t = int(input('Enter time period in terms of years:'))
simple_interest = (p * r * t)/100
print("Simple interest is",simple_interest)