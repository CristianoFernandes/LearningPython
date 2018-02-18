print('#' * 45)
print('#' * 15, 'Exercício 032', '#' * 15)
import datetime

ano = int(input('Digite o ano que deseja analisar: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))
