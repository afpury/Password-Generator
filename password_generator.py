import random
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Enter pass length: "))

password = ""
for i in range(pass_length):
    password += random.choice(elements)

print(password)

a = "1"
b = "2"
print(a) 
# a = a + b
a += b
print(a) 


# import random

# karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# pass_length = int(input("Berapa banyak karakter yang diingankan untuk passwordnya? "))

# password = ""

# for i in range(pass_length):
#     password += random.choice(karakter)

# print(password)

