dados = list()
pessoas = list()
peso = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Você quer continuar [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
for p in pessoas:
    peso.append(p[1])
print(f'O maior peso foi {max(peso)} de ', end='')
for v in pessoas:
    if max(peso) == v[1]:
        print(v[0], end=' ')
print(f'\nO menor peso foi {min(peso)} de ', end='')
for v in pessoas:
    if min(peso) == v[1]:
        print(v[0], end=' ')
