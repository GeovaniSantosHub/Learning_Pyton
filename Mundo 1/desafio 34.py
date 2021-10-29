s = int(input('Qual o valor do seu salário? '))
if s <= 1250:
    a = s + (s * 15 / 100)
else:
    a = s + (s * 10 / 100)
print(f'Voce receberá um aumento de R${a}')