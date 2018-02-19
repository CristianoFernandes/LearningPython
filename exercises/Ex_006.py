print('########## Exercícios de Python ##########')
print('##########    Exercício  006    ##########')
import math

mainNumber = int(input('Digite um número qualquer: '))
print('\033[7;30mO dobro do número {} é {} \033[m'.format(mainNumber, (mainNumber * 2)))
print('\033[7;31mO triplo do número {} é {} \033[m'.format(mainNumber, (mainNumber * 3)))
print('\033[7;30mA metade do número \033[m\033[31;46m {} \033[m\033[7;30m é \033[m\033[31;46m {}\033[m\033[m'.format(
    mainNumber, (mainNumber / 2)))
print('\033[7;31mA raiz quadrada do número {} é {:.2f}\033[m'.format(mainNumber, math.sqrt(mainNumber)))
print('##########################################')
print('##########################################')
