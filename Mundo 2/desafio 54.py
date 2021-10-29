from datetime import date
ano = date.today().year
count = 0
count2 = 0
for c in range (1, 8):
    i = int(input('Em que ano você nasceu?'))
    if ano - i < 18:
        count += 1
    else:
        count2 +=1
print(f'Ao todo tivemos {count} maior de idade e {count2} menores de idade')



