matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite o número da linha {linha} e da coluna {c}: '))
for linha in range(0, 3):
    for c in range(0, 3):
        print('[', f'{matriz[linha][c]:^3}', ']', end='')
    print()
