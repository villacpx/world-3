from uteis import moedas
p = float(input('Digite o preço R$'))
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.dobro(p, False)}')
print(f'A metadede {moedas.moeda(p)} é igual a {moedas.metade(p, True)}')
print(f'Com aumento de 15%, {moedas.moeda(p)} fica com o preço de {moedas.aumento(p, 15, False)}')
print(f'Com o desconto de 10%, {moedas.moeda(p)} fica com o preço de {moedas.desconto(p, 10, True)}')
