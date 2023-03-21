d = {'nome': 'Nathan', 'idade': '16'}
print(d.values())
print(d.keys())
print(d.items())
for k, v in d.items():
    print(f'o {k} é {v}')
d['nome'] = str(input('Outro nome: '))
print(d['nome'])
