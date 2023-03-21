valores = list()
menor = 0
maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}° número: ')))
    if c == 0:
        menor = valores[c]
        maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
if valores.count(maior) == 1:
    print(f'O maior valor digitado foi {maior} na posição:', end=' ')
elif valores.count(maior) > 1:
    print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...', end=' ')
if valores.count(menor) == 1:
    print(f'\nO menor valor digitado foi {menor} na posição:', end=' ')
elif valores.count(menor) > 1:
    print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...', end=' ')
