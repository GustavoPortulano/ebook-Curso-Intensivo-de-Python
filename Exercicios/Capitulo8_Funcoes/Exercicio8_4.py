# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções

'''Exercício 8.4 - Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.'''

def make_shirt(mensagem, tamanho='GG'):
    print("\nTamanho da camiseta: ", tamanho)
    print(mensagem)
make_shirt('Eu amo Python!!')
make_shirt('Complicado!!\n')