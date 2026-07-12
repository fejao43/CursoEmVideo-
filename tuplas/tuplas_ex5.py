
produtos = ('lápis',1.75,
            'caneta',2.0,
            'bolsa', 50.50,
            'tabuada',5.10,
            'livro',10.90,
            'corretivo',3.0)
print('=-'*20)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-='*20)
for i in range(0,len(produtos)):
    if i%2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]}')
           