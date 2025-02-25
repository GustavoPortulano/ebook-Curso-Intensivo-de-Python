# 04 de novembro de 2024
# Segunda-feira, noite nublada, 00h00m

'''Exercício 5.3 - #1 Suponha que um alienigena acabou de ser 
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.  

* Escreva uma instrução if para testar se a cor do alienígena é verde. Se for
mostre uma mensagem inforando que o jogador acabou de ganhar cinco pontos.'''

alien_color = 'green'
if alien_color == 'green':
    print("Você ganhou 5 pontos.")

'''* Escreva uma versão desse programa em que o teste if passe e outro em que
ele falhe.'''
if alien_color == 'red':
    print("Você ganhou 10 pontos.")
if alien_color == 'green':
    print("A cor do ET é verde. Você ganhou 5 pontos.")