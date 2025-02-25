# 18 de novembro de 2024
# Segunda-feira, noite normal
# Pg 146 - Uma lista em um dicionário

# Armazena informações sobre uma pizza que está sendo pedida.
pizza = {'crust':'thick', 'toppings':['nushrooms','extra cheese']}
# Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)
print()

# Segundo exemplo
favorite_languages = {'jean':['python','ruby'],
                      'sarah':['c'],
                      'edward':['ruby','go'],
                      'phil':['python','haskel']}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite laguages are: ")
    for language in languages:
        print("\t " + language.title())

