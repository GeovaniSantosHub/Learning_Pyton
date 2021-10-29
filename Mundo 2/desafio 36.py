preço = float(input('Qual o valor da casa que você deseja comprar ?'))
salario = float(input('Qual o valor do seu salário ?'))
ano = float(input('Em quantos anos você quer pagar ? '))
prestação = preço / (ano * 12)
if prestação <= 30 / 100 * salario:
    print(f'Financiamento é viável, a prestação mensal é de R${prestação}:!')
else:
    print(f'Financiamento inviável, a prestação mensal é de R${prestação}')
