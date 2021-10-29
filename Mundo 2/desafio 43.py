peso = float(input('Qual o seu peso ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / pow (altura , 2)
if imc < 18.5:
    print(f'Seu indice de massa corporal(IMC) é de {imc:.2f}, voê está abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Você está no peso ideal, seu IMC é {imc:.2f}')
elif 25 <= imc < 30:
    print(f'Voc~´e está com SOBREPESO, seu IMC é de {imc:.2f}')
elif 30 <= imc < 40:
    print(f'Você está com OBESIDADE, seu imc é de {imc:.2f}')
else:
    print(f'Você está com OBESIDADE MORBIDA,seu imc é de {imc:.2f}')
