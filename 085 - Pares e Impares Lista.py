num = [[], []]
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(sorted(num))
print(sorted(num[0]))
print(sorted(num[1]))

'''par = []
impar = []
geral = []
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
geral.append(impar)
geral.append(par)
print(sorted(geral[0]))
print(sorted(geral[1]))'''
