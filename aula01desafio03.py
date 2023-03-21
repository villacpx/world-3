from random import randint
a = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Essa é a lista de números gerados pelo computador {a}')
menor = (a[0])
maior = (a[0])
print(f'O maior número é {max(a)} e o menor é {min(a)}')
# deu erro pois não usei o max e o min, não sei aonde achar as funções da tupla
