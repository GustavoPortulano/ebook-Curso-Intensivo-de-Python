# 17 de novembro de 2024
# Domingo, tarde chuvosa. Visita de Thales Vito
# Pg 139 - Percorrendo todos os pares chave-valor com um laço

print("\nPercorrendo todos os pares chave-valor com um laço.")

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

for key, value in user_0.items():
    print("\nkey: " + key)
    print("Value: " + value)

print("\n")

# Segundo exemplo:
print("Segundo exemplo:\n")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'c++'}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")