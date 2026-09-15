tabela = (
    'Flamengo', 'Palmeiras', 'Bahia', 'Cruzeiro', 'Fluminense',
    'Athletico-PR', 'Bragantino', 'Atlético-MG', 'Corinthians', 'São Paulo',
    'Botafogo', 'Santos', 'Vasco', 'Mirassol', 'Grêmio',
    'Internacional', 'Remo', 'Coritiba', 'Chapecoense', 'Vitória'
)

print('A) Os 5 primeiros colocados:')
print(tabela[:5])
print('-' * 40)

print('B) Os últimos 4 colocados:')
print(tabela[-4:])
print('-' * 40)

print('C) Times em ordem alfabética:')
print(sorted(tabela))
print('-' * 40)

posicao_chapeco = tabela.index('Chapecoense') + 1
print(f'D) A Chapecoense está na {posicao_chapeco}ª posição da tabela.')