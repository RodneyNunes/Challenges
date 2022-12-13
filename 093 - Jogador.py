jogador = dict()
gols = list()
jogador['Jogador'] = str(input('Qual o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["Jogador"]} jogou: '))
print(f'Quantos gols {jogador["Jogador"]} fez em cada partida: ')
for c in range(1, partidas + 1):
    gols.append(int(input(f'Gols na partida {c}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])    
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} tem valor {v}')
print('-='*30)
for c in range(0, partidas):
    print(f'  => Na partida {c+1} fez {jogador["gols"][c]} gols')
print(f'O {jogador["Jogador"]} jogou {partidas} partidas e fez {jogador["total"]} gols!!!')