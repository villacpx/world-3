import datetime
pessoa = dict()
pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = (datetime.date.today().year - int(input('Digite seu ano de nascimento: ')))
print('Digite o número da sua carteira de trabalho (0 se não tiver)')
pessoa['CTPS'] = int(input('CTPS: '))
if pessoa['CTPS'] != 0:
    pessoa['Ano contratado'] = int(input('Digite o ano da sua contratação: '))
    pessoa['Salário'] = float(input('Digite seu salário atual: '))
    pessoa['Aposentadoria'] = pessoa["idade"] + (35 - (datetime.date.today().year - pessoa['Ano contratado']))
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
