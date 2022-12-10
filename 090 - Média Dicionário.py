nome = str(input('Qual nome do aluno: '))
media = int(input('Qual a média do aluno: '))
aluno = {'nome':nome, 'média':media}
if media >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print('=-'*20)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')


'''print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["média"]}')
print(f'A situação é {aluno["situação"]}')'''