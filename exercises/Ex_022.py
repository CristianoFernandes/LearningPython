print('#' * 45)
print('#' * 15, 'Exercício 022', '#' * 15)

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analizando seu nome... ')
print('O seu nome em letras maiúsculas é: ', nome.upper())
print('O seu nome em letras minúsculas é: ', nome.lower())
print('O seu nome completo tem ', (len(nome) - (nome.count(' '))), 'letras, sem contar os espaços')
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

# print('O seu primeiro nome tem {} letras'.format(nome.find(' '))) // alternativa
