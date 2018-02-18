print('#' * 45)
print('#' * 15, 'Exercício 033', '#' * 15)

numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))
# Testa menor
menor = numero
if menor > numero2:
    menor = numero2
if menor > numero3:
    menor = numero3

# Testa maior
maior = numero
if maior < numero2:
    maior = numero2
if maior < numero3:
    menor = numero3

print('O menor número é {} e o maior é {}'.format(menor, maior))

# numeros = [numero, numero2, numero3]
# numeros_ordenados=sorted(numeros)
# print('O menor número é {} e o maior é {}'.format(numeros_ordenados[0], numeros_ordenados[2]))
