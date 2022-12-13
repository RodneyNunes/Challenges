from random import randint
from time import sleep
from operator import itemgetter
part1 = {}
part2 = {}
for c in range(1, 5):
    part1[f'jogador{c}'] = randint(1, 6)
part2 = sorted(part1.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados')
for k, v in part1.items():
    print(f'   O {k} tirou {v}')
    sleep(1)    
print('=-'*30)
print('Ranking dos jogadores')
for c in range(0, 4):
    print(f'   {c+1}º lugar - {part2[c][0]} tirou {part2[c][1]}') 
    sleep(1)  