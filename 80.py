lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n >= lista[len(lista)-1]:
        lista.append(n)
    else:
        for cont, valor in enumerate(lista):
            if n < valor:
                lista.insert(cont, n)
                break
print(lista)

'''lista = []
maior = menor = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        maior = menor = n
        lista.append(n)
    else:
        if n >= maior:
            maior = n
            lista.append(n)
        elif n <= menor:
            menor = n
            lista.insert(0, n)
        elif menor < n < maior:
            lista.insert(1, n)
            if n >= lista[2]:
                del(lista[1])
                lista.insert(2, n)
            elif n >= lista[3]:
                del(lista[1])
                lista.insert(3, n)
print(lista)'''