from uteis import moedas
p = float(input('Digite o preço R$'))
print(f'O dobro de R${p} é igual a {moedas.dobro(p)}')
print(f'A metadede R${p} é igual a {moedas.metade(p)}')
print(f'Com aumento de 15%, R${p} fica com o preço de R${moedas.aumento(p, 15)}')
print(f'Com o desconto de 10%, R${p} fica com o preço de R${moedas.desconto(p, 10)}')
