c1 = float(input('Primeiro comprimento:'))
c2 = float(input('Segundo comprimento:'))
c3 = float(input('Terceiro comprimento'))
if c1 < c3 + c2 and c2 < c1 + c3 or c3 < c1 + c2:
    print('Esses comprimentos PODEM formar um triângulo')
else:
    print('Esses segementos NÂO podem formar um triângulo')


