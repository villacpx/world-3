import datetime


def voto(a):
    idade = datetime.date.today().year - ano
    if idade < 16:
        return f'com {idade} anos, o voto é NEGADO'
    elif 18 > idade >= 16:
        return f'com {idade} anos, o voto é OPCIONAL'
    elif 65 > idade >= 18:
        return f'com {idade} anos, o voto é OBRIGATÓRIO'
    elif idade > 65:
        return f'com {idade} anos, o voto é OPCIONAL'


while True:
    ano = int(input('Digite seu ano de nascimento: '))
    print(voto(ano))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = str(input('ERRO! Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta in 'N':
        break
