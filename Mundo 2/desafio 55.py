maior = 0
menor = 0
for p in range(1, 6):
    peso = int(input(f'Peso da {p}° pessoa ?'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é de {maior}kg')
print(f'O menor peso é de {menor}Kg')
