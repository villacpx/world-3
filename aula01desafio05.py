compras = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
           'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('-'*30)
title = 'LISTAGEM DOS PREÇOS'
print(f'{title:^30}')
print('-'*30)
for c in range(0, 18, 2):
    print(f'{compras[c]:.<20}R${compras[c+1]:>8.2f}')
print('-'*30)
