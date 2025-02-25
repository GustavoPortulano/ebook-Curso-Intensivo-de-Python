# 21 de novembro de 2024
# Quinta-feira, noite nublada

'''Exercício 7.2 - Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
oito, exiba uma mensagem dizendo que eles deverão esperar umamesa. caso
contrário, informe que sua mesa está pronta.'''

nr_convidados = int(input("Quantos convidados terá o seu grupo de amigos? "))
if nr_convidados > 8:
    print("Você e seus convidados deverão esperar uma mesa.")
else:
    print("Sua mesa está pronta.")