print('#' * 45)
print('#' * 15, 'Exercício 025', '#' * 15)

nome = str(input('Digite seu nome completo: '))
sobrenome = str(input('Digite o sobrenome procurado: ')).lower()
print('Seu nome possui o sobrenome procurado? {}'.format(sobrenome in nome.lower()))

print('#' * 45)
