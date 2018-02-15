print('#' * 45)
print('#' * 15, 'Exercício 021', '#' * 15)

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analizando seu nome... ')
print('O seu nome em letras maiúsculas é: ', nome.upper())
print('O seu nome em letras minúsculas é: ', nome.lower())
print('O seu nome completo tem ', (len(nome) - (nome.count(' '))), 'sem contar os espaços')
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
