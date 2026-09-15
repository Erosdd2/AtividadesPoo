valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print(f'\nTotal de elementos digitados: {len(valores)}')

valores.sort(reverse=True)
print(f'Valores em ordem decrescente: {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')