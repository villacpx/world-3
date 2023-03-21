import random


def sorteio(list):
    print('Os números sorteados foram:', end=' ')
    for c in range(0, 5):
        numero = random.randint(0, 40)
        if c == 4:
            print(f'{numero}.')
        else:
            print(numero, end=' ')
        numeros.append(numero)


def somapar(list2, numerospares=0):
    for numero in list2:
        if numero % 2 == 0:
            numerospares += numero
    print(f'A soma de todos os números pares são {numerospares}')


numeros = list()
sorteio(numeros)
somapar(numeros)
