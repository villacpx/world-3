from time import sleep
dados = []
pessoas = []
pesado = []
leve = []
pesomaior = pesoleve = 0
while True:
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    peso = float(input('Digite seu peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'NS':
        pergunta = str(input('ERRO, quer continuar? ')).upper().strip()[0]
    if pergunta in 'S':
        sleep(0.5)
        print('...')
        sleep(0.5)
    else:
        break
for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        leve.append(pessoa[0])
        pesado.append(pessoa[0])
        pesoleve = pessoa[1]
        pesomaior = pessoa[1]
    else:
        if pessoa[1] > pesomaior:
            pesomaior = pessoa[1]
            pesado.clear()
            pesado.append(pessoa[0])
        elif pesoleve > pessoa[1]:
            pesoleve = pessoa[1]
            leve.clear()
            leve.append(pessoa[0])
for pessoa in pessoas:
    if pessoa[0] not in pesado and pessoa[1] == pesomaior:
        pesado.append(pessoa[0])
    elif pessoa[0] not in leve and pessoa[1] == pesoleve:
        leve.append(pessoa[0])
if len(pessoas) == 1:
    print('O número de pessoas registrada foi apenas 1')
elif len(pessoas) > 1:
    print(f'O total de pessoas registradas foram: {len(pessoas)} pessoas!')
print(f'O peso mais pesado é {pesomaior} e as pessoas são: {pesado[:]}')
print(f'O peso mais leve é {pesoleve} e as pessoas são: {leve[:]}')
