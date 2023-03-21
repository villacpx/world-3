def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome}, fez {gols} gol(s) no campeonato!')


while True:
    nomeJogador = str(input('Digite o nome do jogador: ')).strip().capitalize()
    quantidadeGols = str(input('Digite a quantidade de gols: '))
    if quantidadeGols.isnumeric() is True:
        quantidadeGols = int(quantidadeGols)
    else:
        quantidadeGols = 0
    if nomeJogador.strip() == '':
        ficha(gols=quantidadeGols)
    else:
        ficha(nomeJogador, quantidadeGols)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('ERRO! Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta in 'N':
        break
    else:
        print()