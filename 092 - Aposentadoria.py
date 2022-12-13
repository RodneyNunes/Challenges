import datetime
cad = {}
cad['Nome'] = str(input('Qual o seu nome: '))
cad['Idade'] = (datetime.date.today().year - int(input('Qual seu ano de nascimento: ')))
cad['CTPS'] = int(input('Qual o número da sua ctps (0 = não tem): '))
if cad['CTPS'] != 0:
    cad['Contratação'] = int(input('Qual o ano de contratação: '))
    cad['Salário'] = float(input('Qual seu salário: R$ '))
    cad['Ano da aposentadoria'] = cad['Contratação'] - datetime.date.today().year + 35 + cad['Idade']
print(cad)
for k, v in cad.items():
    print(f'{k} é {v}')