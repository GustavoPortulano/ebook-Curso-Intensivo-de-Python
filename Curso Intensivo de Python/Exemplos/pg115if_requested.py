# 03 de novembro de 2024
# Domingo, noite nublada

# Verificando se um valor está em uma lista
print("Verificando se um valor está em uma lista.")
requested_toppings = ['mushrooms', 'onions', 'pineaple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print("\n")
# Verificando se um valor não está em uma lista
print("Verificando se um valor não está em uma lista.")
banned_users = ['andrew', 'carolina', 'david']
print(banned_users)
user = 'maria'
print(user.title())
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
print("\n")