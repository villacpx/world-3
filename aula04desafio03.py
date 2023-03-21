def contador(a, b, c):
    print('-=-'*10)
    print(f'CONTANDO DE {a} para {b} de {c} em {c}!!!')
    if c == 0:
        c = 1
    if a < b:
        for c in range(a, b+1, c):
            print(c, end=' ')
        print('FIM')
    elif a > b and c < 0:
        for c in range(a, b-1, c):
            print(c, end=' ')
        print('FIM')
    elif a > b and c > 0:
        for c in range(a, b-1, -c):
            print(c, end=' ')
        print('FIM')


contador(a=1, b=10, c=1)
contador(a=10, b=0, c=-2)
print('-=-'*10)
contador(a=int(input('INÍCIO: ')), b=int(input('FIM: ')), c=int(input('PASSO: ')))
