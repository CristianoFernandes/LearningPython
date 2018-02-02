print('#' * 43)
print('#' * 15, 'DESAFIO 017', '#' * 15)
import math

catetooposto = float(input('Digite a medida do cateto oposto: '))
catetoadjacente = float(input('Digite a medida do cateto adjacente: '))
print('A medida da hipotenusa é: ', math.hypot(catetooposto, catetoadjacente))
print('#' * 43)
