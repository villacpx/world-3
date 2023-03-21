import uteis
from uteis import moedas
p = float(input('Digite o preço R$'))
desconto = int(input('DESCONTO: %'))
aumento = int(input('AUMENTO: %'))
moedas.resumo(p, aumento, desconto)
