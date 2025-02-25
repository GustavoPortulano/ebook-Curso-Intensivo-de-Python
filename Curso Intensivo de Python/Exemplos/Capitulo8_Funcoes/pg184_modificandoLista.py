# 26 de novembro de 2024
# Terça-feira, noite fria
# Ida a Lagoa Santa ao encontro de corretores para a venda da casa
# Pg184 - Modificando uma lista em uma função

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    '''Simula a impressão de cada design, até que não haja mais nenhu.
    Transfere cada design para completed_models após a impressão.'''

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criaçaõ de uma impressão 3D a partir do design
    print("Principal model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Mostra todos os modelos impressos.'''

print("\nThe following models have benn printed: ")
for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


