todos = [[], []]
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        todos[0].append(n)
    elif n % 2 == 1:
        todos[1].append(n)
todos[0].sort()
todos[1].sort()
print(f'Os números pares foram: {todos[0]} e os ímpares foram: {todos[1]}')
