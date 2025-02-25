# 05 de novembro de 2024
# Terça-feira, noite chuvosa

print()

requested_toppings = ['mushrooms', 'green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished makin your pizza!")

print()

requested_toppings = ['mushrooms', 'green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers reght now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished makin your pizza!")
