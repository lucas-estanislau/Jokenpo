import random
import time

# Loop para o progrma continuar inciando após finalizado
while True:
    print('\n')
    print('\033[32m1. PEDRA')
    print('\033[33m2. PAPEL')
    print('\033[34m3. TESOURA\033[m')
    user = int(input('Escolha uma opção:\n'))

    # Converte as opções para os índices da lista
    if user == 1:
        user = 0
    elif user == 2:
        user = 1
    elif user == 3:
        user = 2
    else:
        print('ERROR')
        break
    
    # Imprime animação de "jokenpô"
    print('\n')
    print('JO')
    time.sleep(0.3)
    print('KEN')
    time.sleep(0.3)
    print('PÔ')
    time.sleep(0.3)

    # Lista de opções a serem escolhidas pelo user e o pc
    jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

    # Soreteia um número para escolher um item da lista
    pc = random.randint(0, 2)

    # Imprime a jogada do user e do pc
    print(f'\033[1;35m\n{jokenpo[user]} VS. {jokenpo[pc]}\033[m')

    # Casos pedra
    if user == 0:
        if pc == 0:
            print('\nEMPATE!')
        elif pc == 1:
            print('\nPAPEL VENCE PEDRA! \033[1;31mVOCÊ PERDEU!\033[m')
        elif pc == 2:
            print('\nPEDRA VENCE TESOURA! \033[1;32mVOCÊ VENCEU!\033[m')

    #Casos papel
    if user == 1:
        if pc == 0:
            print('\nPAPEL VENCE PEDRA! \033[1;32mVOCÊ VENCEU!\033[m')
        elif pc == 1:
            print('\nEMPATE!')
        elif pc == 2:
            print('\nTESOURA VENCE PAPEL! \033[1;31mVOCÊ PERDEU!\033[m')

    #Casos tesoura
    if user == 2:
        if pc == 0:
            print('\nPEDRA VENCE TESOURA! \033[1;31mVOCÊ PERDEU!\033[m')
        elif pc == 1:
            print('\nTESOURA VENCE PAPEL! \033[1;32mVOCÊ VENCEU!\033[m')
        elif pc == 2:
            print('\nEMPATE!')