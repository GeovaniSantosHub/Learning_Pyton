num = int(input('digite um número entre 0 e 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print(f'A analisando o número {num}...')
print(f'A sua unidade é {u}\ndesena {d}\ncentena {c}\nmilhar {m}')
