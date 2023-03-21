tupla = ('Abacaxi', 'Berrante', 'Maconheiro')
for c in range(0, len(tupla)):
    a = tupla[c].count('a')
    e = tupla[c].count('e')
    i = tupla[c].count('i')
    o = tupla[c].count('o')
    u = tupla[c].count('u')
    print(f'\n{tupla[c]} tem presente as vogais:')
    if a != 0:
        print('a, '*a, end='')
    if e != 0:
        print('e, '*e, end='')
    if i != 0:
        print('i, '*i, end='')
    if o != 0:
        print('o, '*o, end='')
    if u != 0:
        print('u, '*u, end='')
print('\nACABOU!')
