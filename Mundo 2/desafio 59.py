num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
choice = 0
while choice != 5:
    print('''[1] Somar
[2] Multiplicar
[3]Maior número
[4]Escolher outros números
[5] Sair''')
    choice = int(input('Qual opção ? '))
    if choice == 1:
        print(f'O número {num1} mais {num2} é {num1 + num2}')
    elif choice ==2:
        print(f'O {num1} vezes {num2} é {num1 * num2}')
    elif choice == 3:
        if num1 > num2:
            print(f'O número {num1} é maior')
        else:
            print(f'O número {num2} é maior')
    elif choice == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif choice != (1,5):
        inválido = int(input('Escolha um número catalogado: '))
    print('-=' * 20)




