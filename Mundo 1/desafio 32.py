from datetime import date
data = int(input('Digite um ano:'))
if data == 0:
    data = date.today().year
if data % 4 == 0 and data % 100 != 0:
    print(f'O ano de {data} é bissexto')
else:
    print(f'O ano {data} não é bissexto')