import random

print('#' * 45)
print('#' * 15, 'Exercício 019', '#' * 15)
name1 = input('Digite o nome do aluno 1: ')
name2 = input('Digite o nome do aluno 2: ')
name3 = input('Digite o nome do aluno 3: ')
name4 = input('Digite o nome do aluno 4: ')
lista = [name1, name2, name3, name4]
ordem = random.shuffle(lista)
print('A ordem da apresentação será: {}'.format(lista))
print('#' * 45)
