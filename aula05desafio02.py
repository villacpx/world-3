import math


def factorial(numero, show=False):
    """
    -> Faz o cálculo fatorial do número
    :param numero: número a ser fatoriado
    :param show: True ou False para mostrar a equação
    :param return: volta o numero em fatorial
    """
    fatorial = math.factorial(numero)
    if show is False:
        return fatorial
    else:
        for c in range(numero, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
                return fatorial
            else:
                print(f'{c} x ', end='')


print('-=-'*10)
print(factorial(5, False))
print(factorial(5, True))
print('-=-'*10)
