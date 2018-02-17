print('#' * 45)
print('#' * 15, 'Aula 10', '#' * 15)
import datetime

tempo = int(input('Qual o ano do seu carro? '))
idade = (datetime.date.today().year) - tempo
print(idade)
print('Carro novo' if idade < 5 else 'Carro velho')
print('----- FIM -----')

nome = str(input('Qual é o seu nome? '))
if nome.lower() == 'cristiano':
    print('Bom dia {}! Que nome lindo você tem!!'.format(nome))
else:
    print('Bom dia {}.'.format(nome))
print('#' * 45)

print('----- FIM -----')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(media)
if media >= 6:
    print('Parabens!! Sua média está ok! ')
else:
    print('Ops! Você precisa estudar mais!!')

print('----- FIM -----')
