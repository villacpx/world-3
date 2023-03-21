dados = dict()
gols = list()
jogadores = list()
TotalDeGols = 0
print('-=-'*10)
print(f'{"JOGADOR DE FUTEBOL":^30}')
print('-=-'*10)
while True:
    TotalDeGols = 0
    dados['Nome'] = str(input('Digite o nome do atleta: ')).capitalize()
    dados['quantidade de jogos'] = int(input('Digite a quantidade de jogos que o atleta participou: '))
    for c in range(0, dados['quantidade de jogos']):
        QuantidadeDeGols = int(input(f'Quantos gols ele fez em seu {c+1}° jogo? '))
        gols.append(QuantidadeDeGols)
        dados['Gols'] = gols[:]
        TotalDeGols += QuantidadeDeGols
    dados['Total de gols'] = TotalDeGols
    jogadores.append(dados.copy())
    gols.clear()
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = str(input('ERRO, Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta in 'N':
        break
    else:
        print('...')
print(jogadores)
print('-=-'*15)
print(f'{"Nome":<10} {"Gols":^20} {"Total de Gols":>15} ')
print('-=-'*15)
for Position, CadaJogador in enumerate(jogadores):
    print(f'{Position:<4}', end=' ')
    for dados in CadaJogador.values():
        if dados != CadaJogador['quantidade de jogos']:
            print(f'{str(dados):<15}', end='')
    print()
print('-=-'*15)
while True:
    Especificador = int(input('Mostrar dados de qual jogador? [999 para finalizar] '))
    if Especificador == 999:
        break
    while Especificador > len(jogadores) or Especificador < 0:
        Especificador = int(input('ERRO, Mostrar dados de qual jogador? [999 para finalizar] '))
    print('-=-' * 15)
    print(f' LEVANTAMENTO DO JOGADOR: {jogadores[Especificador]["Nome"]}')
    print('-=-' * 15)
    pos = 0
    while pos != len(jogadores[Especificador]["Gols"]):
        print(f'No seu {pos+1}° jogo, fez {jogadores[Especificador]["Gols"][pos]} gols!')
        pos += 1
    print('-=-' * 15)
