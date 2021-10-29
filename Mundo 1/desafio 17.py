from math import hypot
cato = float(input('Qual o tamanho do cateto oposto?'))
cata = float(input('Qual o tamanho do cateto adjacente?'))
hi = hypot(cato,cata)
print(f'A hipotenusa é:{hi:.2f}')