numeros = (int(input('digite um numero: ')),
           int(input('digite um numero: ')),
           int(input('digite um numero: ')),
           int(input('digite um numero: ')),)
print(f'digitou os valores: {numeros}')
print(f'o 9 apareceu {numeros.count(9)}° vez')
print(f'o valor 3 apareceu na {numeros.index(3)+1} posição')
i = 0
if numeros[0]%2 == 0:
    i += 1
if numeros[1]%2 == 0:
    i+=1
if numeros[2]%2 == 0:
    i+=1
if numeros[3]%2 == 0:
    i+=1
print(f'quantidade de numeros pares: {i}')