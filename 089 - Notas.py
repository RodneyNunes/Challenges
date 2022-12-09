from time import sleep
classe = []
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    classe.append([nome, nota1, nota2])
    cont += 1
    resp = str(input('Quer continuar [s/n]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Digite um valor válido. Quer continuar [s/n]: ')).strip().lower()[0]
    if resp in 'n':
        break
print('=' * 20, 'BOLETIM', '=' * 20)
print(f'Nº Aluno              Nota1   Nota2   Média')
print('-'*45)
for c in range(0, cont):
    print(f'{c+1:<2} {classe[c][0]:20} {classe[c][1]:<3} + {classe[c][2]:^5} = {(classe[c][1] + classe[c][2]) / 2:>4}')
n = int(input('Deseja ver a nota de qual aluno(999 interrompe): '))
while n != 999:
    print(f'{n+1:<2} {classe[n][0]:20} {classe[n][1]:<3} + {classe[n][2]:^5} = {(classe[n][1] + classe[n][2]) / 2:>4}')
    n = int(input('Deseja ver a nota de qual aluno(999 interrompe): '))
print('FINALIZANDO...')
sleep(2)
print('<'*15, 'VOLTE SEMPRE', '>'*15)