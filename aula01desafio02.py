from time import sleep
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
          'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
          'América', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
          'Cuiabá', 'Chapecoense', 'Atlético-GO', 'Avaí', 'Juventude')
cont = 0
chapecoense = (tabela.index('Chapecoense'))
sorteada = sorted(tabela)
print('-=-'*20)
print('Esses foram os 5 primeiros colocados:')
print('-=-'*20)
sleep(1)
for pos, c in enumerate(tabela):
    print(f' {c} ficou em {pos+1}° lugar!')
    cont += 1
    if cont == 5:
        break
sleep(4)
print('-=-'*20)
print('Os últimos 4 colocados foram rebaixado para a divisão B')
print('Os rebaixados foram:')
print('-=-'*20)
sleep(1)
for c in range(16, len(tabela)):
    print(f' O {c+1}° colocado foi: {tabela[c]}')
sleep(4)
print('-=-'*20)
print('Os times que participaram da série A do ano de 2022 foram:')
sleep(1)
print(f'{sorteada}')
sleep(4)
print('-=-'*20)
print(f'Chapecoense ficou em {chapecoense+1}° lugar!')
print('-=-'*20)
