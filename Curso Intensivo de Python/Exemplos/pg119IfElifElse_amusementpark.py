# 04 de novembro de 2024
# Segunda-feira, noite nublada, 23h17m
# Pg 119: sintaxe if-elif-else

print()
age = 12

if age < 4:
    print("Your age is ", age)
    print("Your admission cot is $0.\n")
elif age < 18:
    print("Your age is ", age)
    print("Your admission cost $5.\n")
else:
    print("Your age is ", age)
    print("Your admission cost is $10.\n")

# Segunda maneira:
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your age is ", str(age), "years.")
print("Your admission cost is $" + str(price) + ".\n")