cad = dict()
lista = list()
soma = 0
mulheres = []
acimamed = []
while True:
    cad['Nome'] = str(input('Nome: '))
    cad['Sexo'] = str(input('Sexo [m/f]: ')).strip().lower()[0]
    while cad['Sexo'] not in 'mf':
        cad['Sexo'] = str(input('Digite um valor válido. Sexo [m/f]: ')).strip().lower()[0]
    cad['Idade'] = int(input('Idade: '))
    lista.append(cad.copy())
    soma += cad['Idade']
    resp = str(input('Quer continuar [s/n}: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Digite um valor válido. Quer continuar [s/n}: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-=' * 50)
print(lista)
print('-=' * 50)
media = soma/len(lista)
for v in lista:
    if v['Sexo'] == 'f':
        mulheres.append(v['Nome'])
    if v['Idade'] > media:
        acimamed.append(v['Nome'])
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é {media}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas com idade acima da média são {acimamed}')
    