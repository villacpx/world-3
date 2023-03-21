n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = tuple((n1, n2, n3, n4))
if tupla.count(9) == 0:
    print('O número nove não apareceu!')
elif tupla.count(9) == 1:
    print('O número nove só apareceu 1 vez')
else:
    print(f'O número nove apareceu: {tupla.count(9)} vezes.')
if tupla.count(3) != 0:
    print(f'O número três apareceu na {tupla.index(3)}° posição')
print('Os números pares foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' -> ')
print('ACABOU!')

