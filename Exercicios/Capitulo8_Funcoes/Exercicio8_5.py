# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções

'''Exercício 8.5 - Cidades: Escreva uma função chamada describe_city() qie aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades
diferentes em que pelo menos uma delas não esteja no país default.'''

def describe_city(cidade, pais='Brasil'):
    print("A cidade de ", cidade.title(), " está localizada no ", pais.title() + ".")

describe_city('belo horizonte')
describe_city('campinas')
describe_city('assunção', 'paraguai')