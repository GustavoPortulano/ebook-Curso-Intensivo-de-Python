# 24 de novembro de 2024
# Domingo, noite fria. 
# Ida à igreja
# Capítulo 8: Funções

'''Exercício 8.7 - Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um 
artista e o título de um álbum e deve devolver um dicionário contendo essas 
duas informações. Use a função para criar três dicionários  que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.'''

def make_album(artista, album):
    artista_album = {'cantor':artista, 'disco':album}
    return artista_album

print()
print("Dicionários:")
makeAlbum = make_album('lobão', 'acústico mtv')
print(makeAlbum,"\n")
makeAlbum = make_album('u2', 'best')
print(makeAlbum,"\n")
makeAlbum = make_album('zé ramalho', 'antologia acústica')
print(makeAlbum,"\n")

