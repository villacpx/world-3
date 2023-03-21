def leiaInt(a):
    global n
    n = str(input(a))
    while n.isnumeric() is False:
        print('ERRO, DIGITE APENAS NÚMEROS VÁLIDOS!')
        n = str(input(a))
    if n.isnumeric() is True:
        return n


n = (leiaInt('Digite um número: '))
print(f'Você acabou de digitar {n}!')
