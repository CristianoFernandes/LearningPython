print('########## Exercícios de Python ##########')
print('##########    Exercício  011    ##########')
largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
print('A sua parede tem {:.2f}m x {:.2f}m ou {:.4f}m²'.format(largura, altura, (altura * largura)))
print('Para pintar a sua parede, vc precisará de {:.2f} litros de tinta.'.format((altura * largura) / 2))