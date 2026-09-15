num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

for valor in num:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'\nA lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')