n = int(input('Digite um número:'))
count = 0
for c in range(1, n+1):
    if n % c == 0:
        count += 1
if count == 2:
    print('É primo')
else:
    print('Não é primo')