# 06 de novembro de 2024
# Quarta-feria. Dia nublado

print()

avaiable_toppings = ['mushrooms', 'olives', 'green pepers', 'pepperoni', 'pineaple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")