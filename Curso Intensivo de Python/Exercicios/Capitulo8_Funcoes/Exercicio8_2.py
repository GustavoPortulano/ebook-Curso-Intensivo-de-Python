# 22 de novembro de 2024
# Sexta-feira, noite nublada. 
# Visita das irmãs da igreja
# Capítulo 8: Funções

'''Exercício 8.2 - Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title: A função deve exibir  uma mensagem como Um dos meus livros 
favoritos é alice no país das maravilhas. Chame a função e não se 
esqueça de incluir o título do livro como argumento na chamada da função.'''

def favorite_book(title):
    print("Um dos meus livros favoritos é ", title.title())
    
favorite_book("Canção da Terra distante!")
favorite_book("Duna!")
favorite_book("Shogum!\n")
