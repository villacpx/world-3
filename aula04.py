def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        print(f'na {pos} o valor alterou para {lst[pos]}')
        pos += 1
    print(valores)

 
valores = [1, 2, 4, 6]
dobra(valores)
