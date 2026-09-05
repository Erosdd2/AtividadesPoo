listagem = (
    'Lápis', 2.50,
    'Borracha', 3.50,
    'Caderno', 28.90,
    'Estojo', 18.00,
    'Transferidor', 6.50,
    'Compasso', 14.90,
    'Mochila', 189.90,
    'Canetas', 12.00,
    'Livro', 59.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')

print('-' * 40)