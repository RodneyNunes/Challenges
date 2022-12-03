exp = str(input('Digite um expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')

'''exp = str(input('Digite um expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')'''