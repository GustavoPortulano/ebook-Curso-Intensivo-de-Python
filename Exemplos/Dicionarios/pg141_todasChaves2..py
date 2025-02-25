# 17 de novembro de 2024
# Domingo, noite nublada
# Pg 141 - Percorrendo todas as chaves de um dicionário com um laço.

print("\nPercorrendo todas as chaves de um dicionário com um laço.")
favorite_languages = {'jen':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")
print("\n")

print("Verificando se o nome Erin está na pesquisa.")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")