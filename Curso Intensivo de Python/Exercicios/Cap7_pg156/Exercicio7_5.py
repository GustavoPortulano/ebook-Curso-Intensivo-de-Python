# 21 de novembro de 2024
# Quinta-feira, noite nublada

'''Exercício 7.5 - Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito, se tiver entre 3 e doze anos, o 
ingresso custará 10 dólares, se tiver mais de 12 anos, o ingresso custará 15 
dólares. Escreva um laço em que você pergunte a idade aos usuários e,  então,
informe-lhes o preço do ingresso do cinema.'''

idade = 0

while idade <= 12:
    idade = int(input("qual é a sua idade? "))
    if idade <= 3:
        print("Sua idade é de ", idade, " anos. Seu ingresso é gratuito")
    elif 3 < idade <= 12:
        print("Sua idade é de ", idade, " anos. Seu ingrsso custa $10,00")
    elif idade > 12:
        print("Sua idade é de ", idade, " anos. Seu ingresso custa $15,00.")
    