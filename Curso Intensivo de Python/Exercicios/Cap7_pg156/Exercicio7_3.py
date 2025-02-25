# 21 de novembro de 2024
# Quinta-feira, noite nublada

'''Exercício 7.3 - Múltiplos de 10: Peça um número ao usuário e, em seguida, informe se o 
número é múltiplo de dez ou não.'''

numero = int(input("Digite um número inteiro: "))
if numero % 10 == 0:
    print("O número ", numero, " é divisível por 10.")
else:
    print("O número ", numero, " não é divisível por 10.")