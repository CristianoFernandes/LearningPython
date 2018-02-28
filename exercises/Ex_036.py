print('\033[7;30m' + '#' * 10 + 'Exercícios de Python' + '#' * 10 + '\033[m')
print('\033[7;30m' + '#' * 13 + 'Exercício  036' + '#' * 13 + '\033[m')

print('Olá! Vamos a simulação do seu financimento imobiliário.')
valor = float(input('Digite o valor do imóvel: \n'))
salario = float(input('Digite o valor do seu salário em reais: \n'))
prestacoes = int(input('Digite a quantidade de prestaçoes: '))

if valor / prestacoes > salario * 0.3:
    print('Desculpe. Seu financiamento não foi aprovado.')
else:
    print('Seu financiamento foi aprovado. Parabéns!')
