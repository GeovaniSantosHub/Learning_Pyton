nota1 = float(input('Qual a sua nota ?'))
nota2 = float(input('Qual a sua outra nota ?'))
if (nota1 + nota2) / 2 >= 7:
    print('Você está APROVADO')
elif (nota1 + nota2) / 2 < 5:
    print('Você foi REPROVADO')
elif 5 < (nota1 + nota2) / 2 < 6.9:
    print('Você está de RECUPERAÇÃO')