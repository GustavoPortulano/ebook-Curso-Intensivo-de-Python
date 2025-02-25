# 17 de novembro de 2024
# Domingo, noite nublada
# Pg 141 - Percorrendo as chaves de um dicionário em ordem usando um laço.
# Uso da função sorted()
# Ordenando em ordem alfabética

print("Percorrendo as chaves de um dicionário em ordem usando um laço.")
print("Uso da função sorted()\n")

favorite_languages = {'jean':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
for name in sorted(favorite_languages.keys()):
    print(name.title() + 
          ", thank you for takin the poll.")
print()

