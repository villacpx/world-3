import random
dados = []
jogos = []
nums = 0
q = int(input('Quantos jogos quer mostrar? '))
while True:
    while q != 0:
        while nums != 6:
            n = random.randint(1, 60)
            if n not in dados:
                dados.append(n)
                nums += 1
        dados.sort()
        jogos.append(dados[:])
        dados.clear()
        nums = 0
        q -= 1
    break
for pos, jogo in enumerate(jogos):
    print(f'O {pos+1}° jogo foi: {jogo}')
