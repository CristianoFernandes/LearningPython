print('#' * 45)
print('#' * 15, 'Exercício 030', '#' * 15)

numero = int(input('Digite um número qualquer: '))
print(numero)
print('O número {} é {}'.format(numero, ('ímpar' if (numero % 2 == 1) else 'par')))
