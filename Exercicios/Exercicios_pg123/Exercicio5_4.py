# 05 de novembro de 2024
# Terça-feira, noite chuvosa, 20h59m

'''Exercício 5.4 - Cores de alienígena #2: Escolha uma cor para um alienígena, como foi
feito no exercício 5.3 e escreva uma cadeia if-else.
* Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar 5 pontos por atingir o alienígena.
* Se a cor do alienígena não for verde, mostre uma frase inforando que o
jogador acabou de ganhar 10 pontos.
* Escreva uma versão deste programa que execute o bloco if e outro que
execute o bloco else. '''

print()
cor_alienigena = 'azul'

if cor_alienigena == "verde":
    print("Você ganhou 5 pontos.\n")

if cor_alienigena != 'verde':
    print("Você ganhou 10 pontos.\n")

if cor_alienigena == 'verde':
    print("Você acabou de ganhar 5 pontos por atingir o alienígena.\n")
else:
    print("A cor do alienígena é ", cor_alienigena, ", você ganhou 10 pontos.\n")