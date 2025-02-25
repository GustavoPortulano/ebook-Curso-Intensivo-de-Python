# 17 de novembro de 2024
# Domingo, noite nublada
# Pg 142 - Percorrendo todos os valores de um dicionário com um laço
# Função value()

print("Percorrendo todos os valores de um dicionário com um laço")
print("Função value()")

favorite_languages = {'jean':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
print("The following languages have benn mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()
print("Eliminando repetições.")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()
