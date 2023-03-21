dados = dict()
PessoasRegistradas = list()
SomaIdades = 0
while True:
    dados['nome'] = str(input('Digite seu nome: ')).capitalize()
    dados['sexo'] = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('ERRO! Digite seu sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Digite sua idade atual: '))
    SomaIdades += dados['idade']
    PessoasRegistradas.append(dados.copy())
    repetir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while repetir not in 'SN':
        repetir = str(input('ERRO! Quer continuar? [S/N] ')).strip().upper()[0]
    if repetir == 'N':
        break
    else:
        print('...')
print('-=-'*10)
print(f'{"RESULTADOS":^3}')
print('-=-'*10)
print(f'A quantidade de pessoas registradas foram: {len(PessoasRegistradas)}')
print('-=-'*10)
print(f'A idade média é de {SomaIdades / len(PessoasRegistradas)}')
print('-=-'*10)
print('As mulheres registradas foram:', end=' ')
for mulheres in PessoasRegistradas:
    if mulheres['sexo'] == 'F':
        print(f'[{mulheres["nome"]}]', end=' ')
print()
print('-=-'*10)
print('Lista das pessoas que tem a idade acima da média: ')
for velhos in PessoasRegistradas:
    if velhos['idade']:
        if velhos['idade'] > SomaIdades / len(PessoasRegistradas):
            print(f'{velhos["nome"]} com seus {velhos["idade"]} anos!')
print('-=-'*10)
