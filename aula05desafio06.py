from time import sleep


def ajuda(a):
    global situation
    situation = a
    if situation == 'fim':
        return situation
    else:
        frase = str(f'ACESSANDO O MANUAL DO COMANDO: {a}').upper()
        print('\033[1;31;47m~\033[m'*len(frase))
        print(f'\033[1;31;47m{frase}\033[m')
        print('\033[1;31;47m~\033[m' * len(frase))
        sleep(1)
        print('\033[1;35m'), help(a), print('\033[m')


situation = ''
while situation != 'fim':
    logo = f'{"SISTEMA DE AJUDA PyHELP":^50}'
    print('\033[1;37;40m~\033[m' * len(logo))
    print(f'\033[4;37;40m{logo}\033[m')
    print('\033[1;37;40m~\033[m' * len(logo))
    ajuda(a=(str(input('Função ou Bilbioteca: ')).lower()))
fim = f'{"ATÉ LOGO":^30}'
sleep(1)
print('\033[1;31;47m~\033[m' * len(fim))
print(f'\033[1;31;47m{fim}\033[m')
print('\033[1;31;47m~\033[m' * len(fim))
