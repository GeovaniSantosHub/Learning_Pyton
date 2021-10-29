num = int(input('Digite um número inteiro:'))
print('''Escolha em qual base fazer a converção
 [1]converter para BINÁRIO
 [2]converter para OCTAL
 [3]converter para HEXADECIMAL''')
opção = int(input('Qual sua opção ?'))
if opção == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Essa opção é inválida, tente novamente')
