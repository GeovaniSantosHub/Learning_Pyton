from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0 , 2)
print('''Vamos jogar JOKENPÔ, fracote, quem ganhar domina o universo! HAHAHAHA
      Use:[0] para PEDRA
          [1] para PAPEL
          [2] para TESOURA''')
jogador = int(input('Faça sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if computador == 0:
    if jogador == 0:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]}, EMPATE!')
    elif jogador == 1:
        print(f'Você jogou {itens[jogador]} e a máquina jogou {itens[computador]}, VOCÊ VENCEU!')
    elif jogador == 2:
        print(f'Você jogou {itens[jogador]} e o computador jogou {itens[computador]},VOCÊ PERDEU!')
elif computador == 1:
    if jogador == 0:
        print(f'Você jogou {itens[jogador]} e o PC jogou {itens[computador]},VOCÊ PERDEU!')
    elif jogador == 1:
        print(f'Você jogou {itens[jogador]} e o PC jogou {itens[computador]}, EMPATE!')
    elif jogador == 2:
        print(f'Você jogou {itens[computador]} o PC jogou {itens[computador]}, VOCÊ GANHOU!')
elif computador == 2:
    if jogador == 0:
        print(f'Você jogou {itens[jogador]} e o PC jogou {itens[computador]}, VOCÊ GANHOU!')
    elif jogador == 1:
        print(f'Você jogou {itens[jogador]} e o PC JOGOU {itens[computador]}, VOCÊ PERDEU!')
    elif jogador == 2:
        print(f'Você jogou {itens[computador]} e o PC joogu {itens[computador]}, EMPATE!')
else:
    print(f'Jogada inválida, lê essa porra direito krl :)')




