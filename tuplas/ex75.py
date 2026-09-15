num = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
)

print(f'\nVocê digitou os valores: {num}')

print(f'A) O valor 9 apareceu {num.count(9)} vez(es).')

if 3 in num:
    print(f'B) O primeiro valor 3 foi digitado na {num.index(3) + 1}ª posição.')
else:
    print('B) O valor 3 não foi digitado em nenhuma posição.')

print('C) Os números pares digitados foram: ', end='')
pares = [n for n in num if n % 2 == 0]
if pares:
    print(*pares)
else:
    print('nenhum número par foi digitado.')