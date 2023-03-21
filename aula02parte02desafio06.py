dados = []
alunos = []
num = 'N°'
a = 'Aluno'
m = 'Média'
while True:
    n = str(input('Digite apenas seu primeiro nome: '))
    nota1 = float(input('Digite a nota do primeiro semestre: '))
    nota2 = float(input('Digite a nota do segundo semestre: '))
    dados.append(n)
    dados.append(nota1)
    dados.append(nota2)
    alunos.append(dados[:])
    dados.clear()
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'NS':
        pergunta = str(input('ERRO! Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'S':
        print('...')
    elif pergunta == 'N':
        break
print('_'*21)
print(f'{num:<7} {a:^7} {m:>7}')
for pos, aluno in enumerate(alunos):
    print(f'{pos:<7} {aluno[0]:^7} {(aluno[1] + aluno[2]) / 2:>7}')
print('_'*20)
while True:
    espec = int(input('Qual aluno você deseja ver a nota? 999 para finalizar o programa '))
    if espec == 999:
        break
    else:
        print('-=-'*30)
        print(f'N°: {espec}, Aluno: {alunos[espec][0]}, Notas: {alunos[espec][1]} e {alunos[espec][2]}')
        print('-=-'*30)
