# 18 de novembro de 2024
# Segunda-feira, noite normal

'''Excercício 6.5 - Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo':'egito'.
* Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
para o Egito.
* Use um laço para exibir o nome de cada rio incluido no dicionário.
* Use um laço para exibir o nome de cada país incluido no dicionário.'''

rios = {'nilo':'egito', 'são lourenço':'canadá', 'são francisco':'brasil'}

for rio, pais in rios.items():
    print("O rio ", rio.title(), " percorre o ", pais.title() + ".")