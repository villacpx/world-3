dados = dict()
gols = list()
print('-=-'*10)
print(f'{"JOGADOR DE FUTEBOL":^30}')
print('-=-'*10)
TotalDeGols = 0
dados['Nome'] = str(input('Digite o nome do atleta: ')).capitalize()
dados['quantidade de jogos'] = int(input('Digite a quantidade de jogos que o atleta participou: '))
for c in range(0, dados['quantidade de jogos']):
    QuantidadeDeGols = int(input(f'Quantos gols ele fez em seu {c+1}° jogo? '))
    gols.append(QuantidadeDeGols)
    dados['Gols'] = gols[:]
    TotalDeGols += QuantidadeDeGols
    dados['Total de gols'] = TotalDeGols
print('-=-'*10)
print(f"{dados['Nome']} jogou {dados['quantidade de jogos']} partidas:")
print('-=-'*10)
for c in range(0, len(dados['Gols'])):
    print(f'No seu {c+1}° jogo, ele fez {dados["Gols"][c]} gols')
print('-=-'*10)
