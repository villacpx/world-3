lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
    else:
        print('...')
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'A lista completa digitada foi: {lista}')
print(f'A lista de números pares foi: {pares}')
print(f'A lista de números impares foi: {impares}')

