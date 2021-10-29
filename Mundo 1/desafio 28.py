from random import randint
from time import sleep
computador = randint(0,5)
print('-=' * 33)
print('Tente adivihar em que número eu pensei, ele fica entre 0 e 5...')
print('-=' * 33)
num = int(input('Qual número você acha que é ?'))
print('Precessando...')
sleep(3)
if num == computador:
    print('Parabéns, cria de oráculo, você me derrotou!')
else:
    print('Eu ganhei, agora você será meu escravo sexual HAHAHAHA!')

