# 05 de novembro de 2024
# Terça-feira. Noite nublada

'''Exercício 5.6 - Estágios da vida: Escreva uma cadeia if-elif-else que determine o
estágio da vida de uma pessoa. Defina um valor para a variável age e então:
* Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma
mensagem dizendo quelea é uma criança.
* Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma
mensagem dizendo que ela é um(a) garoto(a).
* Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
* Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulta.
* Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que 
essa pessoa é idosa.'''

print()

age = 85

if 2 < age < 4:
    print("A idade da pessoa é de", age, ". Ela é uma criança.\n")
elif 4 <= age < 13:
    print("A idade da pessoa é de", age, ". Ela é um(a) garoto(a).\n")
elif 13 < age <= 20:
    print("A idade da pessoa é de", age, ". Ela é um(a) adulto(a).\n")
elif 20 < age <= 65:
    print("A idade da pessoa é de", age, ". Ela é um(a) adulto(a).\n")
else:
    print("A idade da pessoa é de", age, ". Ela é um(a) idoso(a).\n")