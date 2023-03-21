expre = str(input('Digite sua expressão: '))
lista = []
for letra in expre:
    if letra in '(':
        lista.append(letra)
    elif letra in ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(letra)
if len(lista) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')
