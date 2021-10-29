n = int(input('Digite o primeiro termo da sua PA:'))
r = int(input('A razão será de:'))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r , r):
    print(f'{c}', end=' ')