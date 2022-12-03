lista = []
c = 0
while True:
    n = (int(input('Digite um número: ')))
    if c == 0 or n <= lista[len(lista)-1]:
        lista.append(n)
    else:
        for cont in range(0, len(lista)):
            if n >= lista[cont]:
                lista.insert(cont, n)
                break
    c += 1
    r = str(input('Quer continuar[s/n]: ')).lower().strip()[0]
    if r == 'n':
        break
print(f'Foi digitado {c} números')
print(lista)
if 5 in lista:
    print(f'O valor 5 foi digitado e aparece {lista.count(5)} vez(es)')
else:
    print('O número 5 não foi digitado')
