print('#' * 45)
print('#' * 15, 'Exercício 023', '#' * 15)

numero = int(input('Digite um número entre 0 e 9999: '))
print(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O número {} possui {} unidades.'.format(numero, u))
print('O número {} possui {} dezenas.'.format(numero, d))
print('O número {} possui {} centenas.'.format(numero, c))
print('O número {} possui {} milhares.'.format(numero, m))
