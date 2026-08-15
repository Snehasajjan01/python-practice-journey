#Write program to convert number from binary to decimal
binary = input("Enter a binary number:")
original_number = binary
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("Decimal of the {}:{}".format(original_number,decimal) )
