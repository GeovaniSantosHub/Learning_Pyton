d = str(input('Digite uma frase:')).strip().upper()
lista = d.strip()
junção = ''.join(lista)
inverso = ''
for c in range(len(junção) - 1,-1, -1 ):
    inverso += junção[c]
print(f'O inverso de {d} é {inverso}')
if inverso == junção:
    print('É um palindromo')
else:
    print('NÃO é um palindromo')