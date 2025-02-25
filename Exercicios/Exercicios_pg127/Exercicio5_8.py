# 08 de novembro de 2024
# Sexta-feira, noite nublada, 20h04m

"""Exercício 5.8 - Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo
o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário:
* Se o nome for 'admin', mostre uma saudação especial, por exemplo, 'Olá
admin, gostaria de ver um relatório de status.
* Caso contrário, mostre uma saudação genérica, como Olá Éric, obrigado por
fazer login novamente."""

print()

usuarios =['ana', 'bela', 'cintia', 'denize', 'erica', 'admin']

for usuario in usuarios:
    if usuario == 'admin':
        print("Olá ", usuario.title(), ". Vocé gostaria de ver uma lista de status?")
    else:
        print("Olá ", usuario.title(), ". Obrigado por fazer login novamente.")

    