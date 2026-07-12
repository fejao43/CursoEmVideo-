def linha():
    print('=-'*45)

linha()
times = 'botafogo', 'corinthians', 'flamengo', 'palmeiras', 'vasco'
print(f'os 5 primeiros: {times}')
linha()
print(f'os primeiros 4 são: {times[0:4]}')
linha()
print(f'em ordem alfabética: {sorted(times)}')
linha()
print(f'o vasco está na {times.index('vasco')} posição')