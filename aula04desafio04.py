from time import sleep


def maior(list):
    print('-=-'*10)
    print(f'Na lista', end=' ')
    for numero in list:
        if numero == list[-1]:
            print(f'{numero}.', end='')
        else:
            print(numero, end=' ')
        sleep(0.2)
    print(f' O maior número detectado foi {max(list)}!')
    print('-=-' * 10)


numeros = list()
while True:
    quantidade = int(input('Quantos números você quer colocar? '))
    for c in range(0, quantidade):
        numeros.append(int(input('Digite o número: ')))
    maior(numeros)
    numeros.clear()
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-=-'*10)
    while pergunta not in 'NS':
        pergunta = str(input('ERRO! Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
