frase = str(input('Escreva algo:')).upper().strip()
a = frase.count('A')
p = frase.find('A') + 1
u = frase.rfind('A') + 1
print(f'Há {a} letras A na sua frase ')
print(f'A letra A aparece pela primeira vez na posição {p}')
print(f'A letra A aparece pela ultima vez na posição {u}')