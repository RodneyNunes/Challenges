matriz = [[], [], []]
for c in range (0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite um valor para posição [ {c}, {d} ]: '))
        matriz[c].append(n)
print('-=' * 20)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()