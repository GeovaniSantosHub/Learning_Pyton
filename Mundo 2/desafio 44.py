preco = float(input('Qual o preço das compras ?'))
print('''Qual opção de pagamento você deseja efetuar
[1] à vista/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcão = int(input('Qual opção deseja ? '))
if opcão == 1:
    print(f'Você pagará {preco * 90 / 100}, pois terá 10% de desconto')
elif opcão == 2:
    print(f'Você pagará {preco * 95 / 100}, pois terá 5% de desconto')
elif opcão == 3:
    print(f' Você pagará {preco} em duas parcelas de {preco / 2}')
else:
    parcel = int(input('Em quantas parcelas ?'))
    print(f'Você pagará {preco * 120 / 100} em {parcel} parcelas de {(preco * 120 / 100) / parcel:.2f}')
