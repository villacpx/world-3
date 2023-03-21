aluno = dict()
escola = 'ESCOLA GUANABARINHA'
print('-=-'*20)
print(f'{escola:^60}')
print('-=-'*20)
aluno['nome'] = str(input('Digite seu nome: '))
aluno['média'] = float(input('Digite sua média: '))
if aluno['média'] < 6.0:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print('-=-'*20)
print(f'O aluno {aluno["nome"]} teve sua média de {aluno["média"]} e sua situação é de {aluno["situação"]}')
print('-=-'*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
