lista = []
impar = []
par = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar [s/n]: ')).lower().strip()[0]
    if resp == 'n':
        break
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(sorted(lista))
print(sorted(par))
print((sorted(impar)))
