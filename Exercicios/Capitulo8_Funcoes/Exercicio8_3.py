# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções

'''Exercício 8.3 - Camiseta: Escreva uma função chamada make-shirt() que aceite um
tamanho de texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
    Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.'''

print("---Função com argumentos posicionais:---")
def make_shirt(tamanho, mensagem):
    print("Tamanho da camiseta: ", tamanho)
    print("Mensagem: ", mensagem)
make_shirt('P', 'Vai dar certo.')

print("\n---Função com argumentos nomeados:---")
make_shirt(tamanho='GG', mensagem='Confie em DEUS!')

