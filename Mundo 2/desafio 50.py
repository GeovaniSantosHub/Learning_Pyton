soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite um número:'))
    if n %2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} números pares é {soma}')
