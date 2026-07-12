palavras = 'aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro'
vogais = 'aeiou'


for i in palavras:
    print(f'\n na palavra {i} temos: ', end='')
    for letras in i:
        if letras.lower() in vogais:
            print(letras,end='')

