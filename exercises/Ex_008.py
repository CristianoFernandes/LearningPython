print('########## Exercícios de Python ##########')
print('##########    Exercício  008    ##########')
distancia = float(input('Digite uma medida em metros: '))
print('A distancia {:.2f}m em decímetros é {:.2f}dm'.format(distancia, (distancia * 10)))
print('A distancia {:.2f}m em centímetros é {:.2f}cm'.format(distancia, (distancia * 100)))
print('A distancia {:.2f}m em milímetros é {:.2f}mm'.format(distancia, (distancia * 1000)))
print('A distancia {:.2f}m em micrômetros é {:.2f}µm'.format(distancia, (distancia * 1000000)))
print('A distancia {:.2f}m em nanômetros é {:.2f}nm'.format(distancia, (distancia * 10000000000)))

print('A distancia {:.2f}m em decâmetros é {:.2f}dam'.format(distancia, (distancia / 10)))
print('A distancia {:.2f}m em hectômetros é {:.3f}hm'.format(distancia, (distancia / 100)))
print('A distancia {:.2f}m em kilômetros é {:.4f}km'.format(distancia, (distancia / 1000)))
print('A distancia {:.2f}m em megametro é {:.6f}Mm'.format(distancia, (distancia / 1000000)))
print('A distancia {:.2f}m em gigâmetro é {:.9f}Gm'.format(distancia, (distancia / 10000000000)))
print('##########################################')
print('##########################################')
