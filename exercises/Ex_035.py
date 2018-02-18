print('#' * 45)
print('#' * 15, 'Exercício 035', '#' * 15)
print('=-' * 11, 'Analisador de Triangulos', '=-' * 11)
segmento1 = float(input('Digite o primeiro segmento 1: '))
segmento2 = float(input('Digite o segundo segmento 2: '))
segmento3 = float(input('Digite o terceiro segmento 3: '))
if segmento1 < (segmento2 + segmento3) and segmento2 < (segmento1 + segmento3) and segmento3 < (segmento1 + segmento2):
    print('Os segmentos 1, 2 e 3 PODEM formar um triangulo. ')
else:
    print('Os segmentos 1, 2 e 3 NÃO PODEM formar uma triangulo. ')
