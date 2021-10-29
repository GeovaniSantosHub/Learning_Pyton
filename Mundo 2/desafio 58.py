from random import randint
computador = randint(0 , 10)
count = 0
print('''        Saudações ser de vida baseada em carbono, eu sou O Computador, é um prazer
jogar com você.
        Deixe-me explicar, é bem simples, irei escolher um número de 0 a 10, e você
terá que advinhar, vamos nessa!
         ''')
num = int(input('choice your number:  '))
acertou = False
while not acertou:
    num = int(input('ERRADO! Try again:  '))
    count += 1
    tentativas = count+1
    if computador == num:
        acertou = True
    else:
        if num > computador:
            print('Menos...')
        else:
            print('Mais..')
print(f'Na mosca! você fez {tentativas} tentativas')




