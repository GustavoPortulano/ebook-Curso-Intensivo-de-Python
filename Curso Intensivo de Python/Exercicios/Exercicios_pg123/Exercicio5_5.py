# 05 de novembro de 2024
# Terça-feira. Noite chuvosa

'''Exercício 5.5 - Cores de alienígenas #3: Transforme sua cadeia if-else do exercício 5.4
em uma cadeia if-elif-else.
* Se o alienígena for verde, mostre uma mensagem inforando que o
jogador ganhou 5 pontos.
* Se o alienígena for amarelo, mostre uma mensagem informando que o
jogador ganhou 10 pontos.
* Se o alienígena for vermelho, mostre uma mensagem informando que o
jogador ganhou 15 pontos.
* Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena. '''

print()

cor_alienigena = 'verde'
if cor_alienigena == 'verde':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 5 pontos.\n")
elif cor_alienigena == 'amarela':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 10 pontos.\n")
else:
    print("A cor do alienígena é vermelha", cor_alienigena, ". Você ganhou 15 pontos.\n")

cor_alienigena = 'amarela'
if cor_alienigena == 'verde':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 5 pontos.\n")
elif cor_alienigena == 'amarela':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 10 pontos.\n")
else:
    print("A cor do alienígena é vermelha", cor_alienigena, ". Você ganhou 15 pontos.\n")

cor_alienigena = 'vermelha'
if cor_alienigena == 'verde':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 5 pontos.\n")
elif cor_alienigena == 'amarela':
    print("A cor do alienígena é", cor_alienigena, ". Você ganhou 10 pontos.\n")
else:
    print("A cor do alienígena é vermelha", cor_alienigena, ". Você ganhou 15 pontos.\n")