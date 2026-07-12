number = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

number_ask = int(input('digite um numero entre 0 e 20 '))
while number_ask not in number:
     number_ask = int(input('Tente novamente, digite um numero entre 0 e 20 '))

match number_ask:
    case 1: print('um')
    case 2: print('dois')
    case 3: print('três')
    case 4: print('quatro')
    case 5: print('cinco')
    case 6: print('seis')
    case 7: print('sete')
    case 8: print('oito')
    case 9: print('nove')
    case 10: print('dez')
    case 11: print('onze')
    case 12: print('doze')
    case 13: print('treze')
    case 14: print('cartoze')
    case 15: print('quinze')
    case 16: print('dezesseis')
    case 17: print('dezesete')
    case 18: print('dezoito')
    case 19: print('dezenove')
    case 20: print('vinte')