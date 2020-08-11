## por Israel Augusto

import requests
from random import choice
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

texto = requests.get(url).text.split()

def desenha():
    print(forca[len(erradas)])
    for i in palavra:
        if i in certas:
            print(i, end = ' ')
        else:
            print('*', end = ' ')
    print()

forca = ['''
    +======+
           |
           |
           |
           |
           |
    ========''',
         '''
    +======+
    |      |
           |
           |
           |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
           |
           |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
    |      |
           |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
   /|      |
           |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
   /|\     |
           |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
   /|\     |
   /       |
           |
    ========''',
         '''
    +======+
    |      |
    O      |
   /|\     |
   / \     |
           |
    ========''']

continua = 1

while(continua):
##    sorteada = choice(palavra)
    continua = int(input('Deseja continuar?\n 0.Nao 1.Sim: '))
    
    if continua:
        certas = ''
        erradas = ''

        palavra = choice(texto)
##        palavra = input('Insira a palavra secreta: ')

        for i in range(100):
            letra = input('Letra: ')
            
            if letra in palavra and letra not in certas:
                certas += letra
            elif letra in palavra and letra in certas:
                print('Você ja tentou esta letra :)')
            elif letra not in palavra and letra not in erradas:
                print('Você errou :)')
                erradas += letra
            elif letra not in palavra and letra in erradas:
                print('Você ja tentou esta letra :)')

            desenha()
            
            if len(erradas) == len(forca) - 1:
                print('Fim de jogo.')
                print('A palavra era: ' + palavra)
                break
     
            if set(certas) == set(palavra):
                print('Você ganhou!!!')
                break
