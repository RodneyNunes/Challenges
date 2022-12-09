from random import randint
from time import sleep
quant = int(input('Quantos jogos deseja fazer: '))
aux = []
princ = []
for c in range(0, quant):
    for i in range(0, 6):
        n = randint(1, 60)
        while n in aux:
            n = randint(1, 60)
        aux.append(n)
    princ.append(aux[:])
    aux.clear()
    print(f'jogo {c+1}: {sorted(princ[c])}')
    sleep(1)