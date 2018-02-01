print('########## Exercícios de Python ##########')
print('##########    Exercício  010    ##########')
money = float(input('Quanto você tem na carteira? R$'))
dolar = 3.25
print('Com R$', money, 'você pode comprar U$', '{:.2f}'.format(money / dolar), 'dólares')
