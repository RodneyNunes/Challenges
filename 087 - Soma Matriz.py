matriz = [[], [], []]
par = list()
l2 = []
somat = 0
for c in range (0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite um valor para posição [ {c}, {d} ]: '))
        matriz[c].append(n)
        if n % 2 == 0:
            par.append(n)
print('-=' * 20)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()
for c in range (0, 3):
    somat += matriz[c][2]
print(f'A soma dos números pares é {sum(par)}')
print(f'A soma dos números da 3º coluna é {somat}')
print(f'A maior número 2º linha é {max(matriz[1])}')
