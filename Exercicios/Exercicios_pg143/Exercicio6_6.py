# 18 de novembro de 2024
# Segunda-feira, noite normal.

'''Exercicio 6.6: Enquete: Utilize o código em favorite_languages.py.
* Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.
* Percorra a lista de pessoas que devem participar da enquete. Se elas já
tiverem respondido à enquete, mosre uma mensagem agradecendo_lhes por
responder. Se ainda não participaram da enquete, apresene uma mensagem
convidando-as a responder.'''

print()
print("Lista de participantes:")
participantes = ['ana', 'blenda', 'carla', 'davi', 'elton']
print(participantes)

print("Diconário referente à pesquisa:")
pesquisa = {'jean':'python', 'edward':'ruby', 'ana':'c++', 'davi':'PHP'}
print(pesquisa)
print()
for nome, linguagem in pesquisa.items():
    if nome in participantes:
        print(nome.title(), "tem como linguagem favorita ", linguagem + ".")
        print("Obrigado por participar de nossa pesquisa!\n")
    else:
        print(nome.title(), " por favor, participe de nossa pesquisa.\n")
    