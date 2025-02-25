# 17 de novembro de 2024. 
# Domingo, tarde chuvosa. Visita de Thales Vitor
# Pg 134 - exemplo 2: Modificando valores de um dicionário

print("\nModificando valores de um dicionário.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua 
# velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienígena rápido
    x_increment = 3
# A nova posição é a posição antiga somada ao incremento.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("\nNew x-position: " + str(alien_0['x_position']) +"\n")