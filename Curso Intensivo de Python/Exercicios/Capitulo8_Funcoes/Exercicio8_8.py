# 24 de novembro de 2024
# Domingo, noite fria. 
# Ida à igreja
# Capítulo 8: Funções

'''Exercício 8.8 - Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título do álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.'''

def make_album(artista, album):
    artista_album = {'cantor':artista, 'disco':album}
    return artista_album
   
while True:
    print("\nDigite o nome do artista e o nome do seu álbum:")
    print("Digite (*) para sair:")
    nome_artista = str(input("Nome do artista: ")).title()
    if nome_artista == '*': break
    nome_album = str(input("Nome do álbum: ")).title()
    if nome_album == '*': break
    artista_album = make_album(nome_artista, nome_album)

print("\nDicionário:")
print(artista_album)


