l1 = float(input('Lado 1:'))
l2 = float(input('lado 2:'))
l3 = float(input('lado 3:'))
if l1 < l2 + l3 or l2 < l1 + l3 and l3 < l1 + l2:
    print('O triangulô é viável',  end='')
    if l1 == l2 == l3:
        print('Triângulo equilátero')
    elif l1 != l2 != l3:
        print('Triângulo escaleno')
    else:
        print('Isóceles')
else:
    print('O triangulo não é viável')
