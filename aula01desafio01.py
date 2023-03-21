from time import sleep
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resultado = 'RESULTADO'
print('-=-'*20)
while True:
    n = int(input('Digite um número de 0 a 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente novamente, digite um número de 0 a 20: '))
    print('\n')
    sleep(0.4)
    print(f'{resultado:-^20}')
    print('\n')
    sleep(0.6)
    print(f'o número {n} escrito por extenso é {extenso[n]}')
    print('\n')
    print('-'*20)
    print('[ 1 ] Digitar outro número'
          '\n[ 2 ] Fechar o programa')
    pergunta = int(input(' '))
    if pergunta == 2:
        break
    if pergunta == 1:
        print('Ok', end=', ')
sleep(1)
print('Obrigado por usar nosso programa')
