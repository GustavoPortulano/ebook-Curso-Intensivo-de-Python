# 17 de novembro de 2024. 
# Domingo, tarde chuvosa. Visita de Thales Vitor

'''Exercício 6.1 - Pessoa: Use um diconário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a 
cidade em que ela vive. Você deverá ter chaves como first_name, last_name, age e city.
Mostre cada informação armazenada em seu dicionário.'''

# Criando o dicionário.
pessoa = {'nome': 'júlio', 'sobrenome': 'césar', 'idade': 50, 'cidade': 'roma'}

print("\nNome:      ", pessoa['nome'].title(),
      "\nSobrenome: ", pessoa['sobrenome'].title(),
      "\nIdade:     ", pessoa['idade'], "anos.",
      "\nCidade:    ", pessoa['cidade'].title())
