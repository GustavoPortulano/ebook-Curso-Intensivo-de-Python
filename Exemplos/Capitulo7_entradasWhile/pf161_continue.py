# 21 de novembro de 2024
# Quinta-feira, noite nublada
# Pg 161: Usando continue em um laço


curent_number = 0
while curent_number < 10:
    curent_number += 1
    if curent_number % 2 == 0:
        continue
    print(curent_number)