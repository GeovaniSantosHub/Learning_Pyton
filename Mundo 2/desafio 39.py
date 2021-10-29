from datetime import date
ano = int(input('Em que ano você nasceu ?'))
agora = date.today().year
idade = agora - ano
if agora - ano == 18:
    print('Você já está com 18 anos,vá se alistar!')
elif agora - ano > 18:
    saldo = idade - 18
    print(f'MUITO BEM!SEU PRAZO DE ALISTAMENTO JÁ PASSOU, VÁ SE ALISTAR SEU VAGABUNDO, já se passaram {saldo} ano(s)')
    print(f'Seu alistamento foi em {agora - saldo}')
elif agora - ano < 18:
    saldo = 18 - idade
    print(f'Você possui menos de 18 anos,terá que se alistar daqui a {saldo} ano(s) ')
    print(f'Seu alistamento será no ano de {agora + saldo}')