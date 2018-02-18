print('#' * 45)
print('#' * 15, 'Exercício 034', '#' * 15)
salario = float(input('Digite o valor do salário: R$'))
if (salario <= 1.250):
    print('O salário reajustado é {:.2f}'.format(salario * 1.15))
else:
    print('O salário reajustado é {:.2f}'.format(salario * 1.10))
