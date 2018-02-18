print('#' * 45)
print('#' * 15, 'Exercício 028', '#' * 15)

import random

numero = int(random.randint(1, 5))
numero2 = int(input('Tente advinhar um número de 1 a 5: '))
if numero == numero2:
    print('Você acertou em cheio! ')
else:
    print('Você errou. O número é {}'.format(numero))
print('----- FIM -----')
