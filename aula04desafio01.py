def area(a, b):
    valor = a * b
    print('-=-'*10)
    print(f'a medida do seu terreno foi de {a}m²x{b}m², a área de seu terreno é de: {valor:.2f}')
    print('-=-'*10)


area(a=(float(input('Digite o valor do comprimento do terreno: '))),
     b=float(input('Digite o valor da largura do seu terreno: ')))
