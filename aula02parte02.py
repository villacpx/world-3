dados = list()
pessoas = list()
while True:
    nome = str(input('')).strip().capitalize()
    idade = int(input(''))
    if idade == 0:
        break
    dados.append(nome)
    dados.append(idade)
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)
