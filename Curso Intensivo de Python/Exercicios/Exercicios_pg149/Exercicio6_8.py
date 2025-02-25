# 20 de novembro de 2024
# Quarta-feira, noite chuvosa
# Samuel dormiu em casa
# Omar almoçou em casa
# Ida a Lagoa Santa após receber ligação de que estavam furtando madeira na casa.

'''Exercício 6.8 - Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada diconário, inclua
o tipo do animal e o nome do dono. Armazene esses diconários em uma lista
chamada pets. Em seguida, percorra sua lista com um  laço e, à medida que
fizer isso, apresente tudo o que sabe sobre cada animal de estimação.'''

jerry = {'nome do animal':'jerry', 'espécie':'rato','dono':'hanna barbera','tamanho':'pequeno'}
tom = {'nome do animal':'tom', 'espécie':'gato', 'dono':'hanna barbera', 'tamanho':'médio'}
snopy = {'nome do animal':'snopy', 'espécie':'cachorro', 'dono':'charlie brown','tamanho':'médio'}

pets = [jerry, tom, snopy]

for pet in pets:
    if pet == jerry:
        print("Nome do animal: ", pet['nome do animal'].title(),
              "\nEspécie do animal: ", pet['espécie'],
              "\nDono do animal: ", pet['dono'].title(),
              "\nTamanho do animal: ", pet['tamanho'], "\n")
    elif pet == tom:
        print("Nome do animal: ", pet['nome do animal'].title(),
              "\nEspécie do animal: ", pet['espécie'],
              "\nDono do animal: ", pet['dono'].title(),
              "\nTamanho do animal: ", pet['tamanho'], "\n")
    elif pet == snopy:
        print("Nome do animal: ", pet['nome do animal'].title(),
              "\nEspécie do animal: ", pet['espécie'],
              "\nDono do animal: ", pet['dono'].title(),
              "\nTamanho do animal: ", pet['tamanho'],"\n")