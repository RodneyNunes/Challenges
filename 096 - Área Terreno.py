def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é {a:.2f} m².')

l = float(input('Qual a LARGURA do terreno em metros: '))
c = float(input('Qual o COMPRIMENTO do terreno em metros: '))
area(l,c)
