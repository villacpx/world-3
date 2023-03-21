import random
jogadas2 = {}
ordem = []
numordem = []
maior = 0
for c in range(0, 4):
    n = random.randint(1, 6)
    jogadas2[f'{c}'] = n
    print(f'O {c}° jogador jogou e caiu o número {n}')
for k, v in jogadas2.items():
    if k == '0' or v > numordem[-1]:
        ordem.append(k)
        numordem.append(v)
    else:
        pos = 0
        while pos != len(numordem):
            if v <= numordem[pos]:
                numordem.insert(pos, v)
                ordem.insert(pos, k)
                break
            pos += 1
numordem.reverse()
ordem.reverse()
for r in range(0, len(numordem)):
    print(f'Ficou em {r+1}° lugar o Jogador N°{ordem[r]} com o valor {numordem[r]}')
