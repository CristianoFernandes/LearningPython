print('#' * 45)
print('#' * 15, 'Exercício 028', '#' * 15)
velocidade = int(input('Qual a velocidade atual do seu carro?'))
if velocidade <= 80:
    print('Boa viagem. Sua velocidade está compatível com a via. ')
else:
    diferenca = velocidade - 80
    print('Vc foi MULTADO. A velocidade máxima desta via é 80km/h. O valor da multa é R${:.2f}'.format(diferenca * 7))
print('----- FIM -----')
