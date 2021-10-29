idade = int(input('qual sua idade ?'))
if idade <= 9:
    print('Você faz parte do clube mirim de natação')
elif 10 <= idade <= 14:
    print('Você faz parte do clube infantil de natação')
elif 15 <= idade  <= 19:
    print('Você faz parte do clube JUNIOR de natação')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
