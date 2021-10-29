v = float(input('Qual a velocidade do veiculo ?'))
if v <= 80:
    print('Velocidade permitida, tenha um bom dia!')
else:
    multa = (v - 80) * 7
    print(f'velocidade acima do permitido, você será mutaldo em R${multa}')