def notas(list, sit=False):
    """"
    -> função: Analisar várias notas, mostrar dados e situações
    :param list: tem a função de ler a lista com as notas para mostrar os resultados
    :param sit: recebe os valores False ou True: indica se quer receber ou não a situação do aluno
    :return: não volta nada
    """
    global lista
    lista['total'] = len(notasAlunos)
    lista['maior nota'] = max(notasAlunos)
    lista['menor nota'] = min(notasAlunos)
    lista['média'] = sum(notasAlunos) / len(notasAlunos)
    if sit is True:
        if lista['média'] > 6.5:
            lista['situação'] = 'APROVADO'
        if 5.0 <= lista['média'] <= 6.5:
            lista['situação'] = 'RECUPERAÇÃO'
        if lista['média'] < 5.0:
            lista['situação'] = 'REPROVADO'


lista = dict()
notasAlunos = list()
total = 0
quantidade = int(input('Quantas notas quer digitar? '))
for c in range(0, quantidade):
    notasAlunos.append(int(input(f'Digite a {c+1} nota! ')))
mostrar = str(input('Quer mostrar sua situação? [S/N] ')).strip().upper()[0]
while mostrar not in 'NS':
    mostrar = str(input('Quer mostrar sua situação? [S/N] ')).strip().upper()[0]
if mostrar in 'S':
    notas(notasAlunos, sit=True)
else:
    notas(notasAlunos)
print(lista)
