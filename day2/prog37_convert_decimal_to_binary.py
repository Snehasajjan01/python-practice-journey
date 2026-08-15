#Write proogrm to convert number from decimal to binary
n = int(input('Enter a number:'))
original_number = n
binary = ""
while n != 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2
print("Binary number of {} is:{}".format (original_number,binary))