geral = list()
jogador = dict()
gols = list()
while True:
    jogador['jogador'] = str(input('Qual o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["jogador"]} jogou: '))
    print(f'Quantos gols {jogador["jogador"]} fez em cada partida: ')
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Gols na partida {c}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    gols.clear()
    geral.append(jogador.copy())
    resp = str(input('Quer continuar [s/n]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Digite um valor válido. Quer continuar [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-=' * 20)
print(geral)
print('-=' * 20)
print(f'{"Cód":<3} {"Nome":<18} {"Gols":<18} {"Total"}')
print('-' * 50)
for c, v in enumerate(geral):
    print(f'{c+1:^3} {v["jogador"]:<18} {v["gols"]!s:<20s} {v["total"]}')
r = str(input('Deseja continuar[s/n]: ')).strip().lower()[0]
while r not in 'sn':
        r = str(input('Digite um valor válido. Deseja continuar [s/n]: ')).strip().lower()[0]
while r != 'n':
    n = int(input('Deseja mostrar dados de qual jogador[Cód]: '))
    while n not in range(1, len(geral)+1):
        n = int(input('Digite um valor válido. Deseja mostrar dados de qual jogador[Cód]: '))
    print(f'Levantamento do jogador {geral[n-1]["jogador"].upper()}')
    for c, v in enumerate(geral[n-1]['gols']):
        print(f'   => No jogo {c+1} fez {v} gols')
    r = str(input('Deseja continuar[s/n]: ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('Digite um valor válido. Deseja continuar [s/n]: ')).strip().lower()[0]
print('<<<ENCERRADO>>>')