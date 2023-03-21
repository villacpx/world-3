lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
    else:
        print('...')
print(f'A quantidade de números digitados foram: {len(lista)}')
print('-=-'*20)
lista.sort(reverse=True)
print(lista)
print('-=-'*20)
if 5 not in lista:
    print('Não encontrei número 5 nessa lista!')
else:
    print(f'Encontrei 5 na lista, a quantidade de 5 na lista é: {lista.count(5)}')
