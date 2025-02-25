# 24 de novembro de 2024
# Domingo, noite fria. 
# Ida à igreja
# Capítulo 8: Funções

'''Exercício 8.6 - Nomes de cidades: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile".
    Chame sua função com pelo menos três pares cidades-país e apresente o 
valor devolvido.'''

print()
def city_country(cidade, pais):
    cidade_pais = cidade + ' ' + pais
    return cidade_pais.title()

cidadeEpais = city_country('brasilia,','brasil')
print(cidadeEpais)
cidadeEpais = city_country('buenos aires,','argentina')
print(cidadeEpais)
cidadeEpais = city_country('havana,','cuba')
print(cidadeEpais)


   