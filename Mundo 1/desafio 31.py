d = float(input('Qual a distância da sua viagem ?'))
if d <= 200:
    print(f'Sua viagem de {d}km custará {d * 0.5}')
else:
    print(f'Sua viagem de {d}km custará {d * 0.45}')