# 03 de novembro de 2024
# Domingo. Dia nublado

'''Exercício 4.13 - Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
de cominda. Pense em conco pratos simples e armazenoos em uma tupla.
* Use um laço for para exibir cada prato oferecido pelo restaurante.
* Tente modificar um dos ítens e certifique-se de que Python rejeito a mudança.
* O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
segida, use um laço for para exibir um dos ítens do cardápio revisado. '''

print()
cardapio = ('tutu', 'feijão tropeiro', 'vaca atolada', 'frango com pequi', 'churrasco')
print("Lista de pratos oferecidos:")
for prato in cardapio:
    print("Opção para o almoço/jantar: ", prato.title())

print()
print("Novas opções:")
cardapio = ('feijoada', 'costelinha com orapronobis', 'vaca atolada', 'frango com pequi', 'churrasco')
print("Lista de pratos oferecidos:")
for prato in cardapio:
    print("Opção para o almoço/jantar: ", prato.title())