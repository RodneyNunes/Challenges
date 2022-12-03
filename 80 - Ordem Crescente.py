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
