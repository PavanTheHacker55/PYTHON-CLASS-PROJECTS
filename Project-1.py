import os

os.system('cls')

print("                         WELCOME TO THIS BASE CONVERTER APP")
print("                         ==================================")

print()
number = int(input("Enter A Number In Decimal Format: "))

os.system('cls')
print("                                 RESULT")
print()
print(number,"Is In Decimal Format",number)
print()
print(number,"Is In Binary Format", bin(number))
print()
print(number,"Is In Octal Format", oct(number))
print()
print(number,"Is In Hexa Decimal Format", hex(number))