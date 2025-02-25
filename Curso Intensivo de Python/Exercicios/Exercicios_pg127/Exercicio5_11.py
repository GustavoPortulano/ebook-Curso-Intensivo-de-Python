# 08 de novembro de 2024
# Sexta-feira. Noite nublada

'''Exercicio 5.11 - Números ordinais: Números ordinais indicam sua posição em uma lista,
por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa
língua termina em th, exceto 1, 2 e 3.
* Armazene os números de 1 a 9 em uma lista,
* Percorra a lista com um laço.
* Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
para cada número ordinal. Sua saída deverá conter '1st 2nd 3rd 4th..., e cada 
resultado deve estar em uma linha separada.'''

print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero == 1:
        print(str(numero) + "st")
    elif numero == 2:
        print(str(numero) + "nd")
    elif numero == 3:
        print(str(numero) + 'rd')
    else:
        print(str(numero) + "th")