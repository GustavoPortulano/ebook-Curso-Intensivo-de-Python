# 17 de novembro de 2024
# Domingo, noite nublada.
# Pg 140 - Percorrendo todas as chaves de um dicionário com um laço
# Método key()

print("\nPercorrendo todas as chaves de um dicionário com um laço Método key()\n")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
print(favorite_languages)
for name in favorite_languages.keys():
    print(name.title())
print("\n")

print("Segunda forma do laço:")
for name in favorite_languages:
    print(name)


