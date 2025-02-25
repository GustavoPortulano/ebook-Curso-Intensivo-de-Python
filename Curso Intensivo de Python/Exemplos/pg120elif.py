# 04 de novembro de 2024
# Segunda-feira, noite nublada, 23h17m
# Pg 120: usando vários blocos elif

print()
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your age is ", age, "years.")
print("Your admission cost is $" + str(price) + ".\n")