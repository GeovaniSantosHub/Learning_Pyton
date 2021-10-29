soma = 0
count = 0
maioridade = 0
nomevelho = ''
for c in range(1, 5):
    print(f'----{c}° pessoa----')
    nome = str(input('Qual o seu nome ?')).strip()
    idade = int(input('Qual sua idade ?'))
    sexo = str(input('Qual o seu sexo [M/F] ?')).strip()
    soma += idade
    if sexo in 'Mm' and c == 1:
        maioridade = idade
        nomevelho = nome
    else:
        if idade > maioridade:
            maioridade = idade
            nomevelho = nome
    if sexo in 'Ff':
        count +=1
media = soma / 4
print(f''' 
A média das idades é: {media}'
numero de mulheres são: {count}
A pessoa mais velha é: {nomevelho} com {maioridade} anos''')








