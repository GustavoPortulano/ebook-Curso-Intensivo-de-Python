# 18 de novembro de 2024
# Segunda-feira, noite normal
# Uso da função range()

print("Uso da função range()")
# Cria uma lista vazia para armazenar alienígenas:
aliens = []
# Cria 30 alienígenas verdes:
for alien_number in range(30):
    new_alien = {'color':'green', 'pointes':5, 'speed':'slow'}
    aliens.append(new_alien)
    print(alien_number, new_alien)

print()

for alien in aliens[:5]:
    print(alien)

print()
# Mostra quantos aliens foram criados:
print("Total number of aliens: " + str(len(aliens)))

print()
# Pg 145 - Modificando as caractarísticas dos alienígenas
# Cria 30 alienígenas verdes
# Cria uma lista vazia para armazenar os alienígenas

print("Modificando alienígenas:")
alienigenas = []
for alien_number in range(0,30):
    novo_alien = {'cor':'verde', 'pontos':5, 'velocidade':'lento'}
    alienigenas.append(novo_alien)

for alienigena in alienigenas[0:5]:
    if alienigena['cor'] == 'verde':
        alienigena['cor'] = 'amarelo'
        alienigena['velocidade'] = 'médio'
        alienigena['pontos'] = 10

for alienigena in alienigenas[5:10]:
    if alienigena['cor'] == 'verde':
        alienigena['cor'] = 'vermelha'
        alienigena['velocidade'] = 'rápido'
        alienigena['pontos'] = 15

# Mostra os 5 primeiros alienígenas:
for alienigena in alienigenas[0:15]:
    print(alienigena)



