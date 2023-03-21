matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna2 = maior = 0
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite o número da linha {linha+1} e da coluna {c+1}: '))
        if c == 2:
            coluna2 += matriz[linha][c]
for linha in range(0, 3):
    for c in range(0, 3):
        print('[', f'{matriz[linha][c]:^3}', ']', end='')
    print()
for pos, linha in enumerate(matriz):
    for num in linha:
        if num % 2 == 0:
            soma += num
    if pos == 1:
        for pos2, num in enumerate(linha):
            if pos2 == 0:
                maior = num
            else:
                if num > maior:
                    maior = num
print(f'A soma dos números pares dessa matriz é {soma}')
print(f'A soma da terceira linha dessa matriz é {coluna2}')
print(f'O maior número da segunda linha é {maior}')


