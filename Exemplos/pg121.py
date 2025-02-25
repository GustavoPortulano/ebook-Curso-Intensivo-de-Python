# 04 de novembro de 2024
# Segunda-feira, noite nublada, 23h17m
# Pg 121: Omitindo o bloco else

print()
age = 12

if age < 4:
    price = 0
if age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your age is ", age, " years.")
print("Your adimission cost is $" + str(price) + ".\n")