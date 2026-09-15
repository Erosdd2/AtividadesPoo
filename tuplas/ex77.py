palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'besta',
    'trabalho', 'mercado', 'esnobe', 'futuro'
)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')