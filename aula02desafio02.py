valores = []
pergunta1 = ''
while True:
    n = (int(input('Digite um número: ')))
    if valores.count(n) != 0:
        valores.remove(n)
        print('Valor duplicado. Seu número não foi registrado')
    valores.append(n)
    valores.sort()
    pergunta1 = (str(input('Quer continuar? [S/N] ')).strip().upper()[0])
    while pergunta1 not in 'NS':
        print('ERRO, TENTE NOVAMENTE')
        pergunta1 = (str(input('Quer continuar? [S/N] ')).strip().upper()[0])
    if pergunta1 == 'S':
        print('...')
    elif pergunta1 == 'N':
        break
print(valores)
