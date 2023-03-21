from uteis import moedas
p = float(input('Digite o preço R$'))
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.moeda(moedas.dobro(p))}')
print(f'A metadede {moedas.moeda(p)} é igual a {moedas.moeda(moedas.metade(p))}')
print(f'Com aumento de 15%, {moedas.moeda(p)} fica com o preço de {moedas.moeda(moedas.aumento(p, 15))}')
print(f'Com o desconto de 10%, {moedas.moeda(p)} fica com o preço de {moedas.moeda(moedas.desconto(p, 10))}')
