print('########## Exercícios de Python ##########')
print('##########    Exercício  012    ##########')
preço = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto a se aplicar: '))
print('O produto cujo preço é R${:.2f} está com {}% de desconto e sai por R${}'.format(preço, desconto, (
            preço - (preço * desconto / 100))))
