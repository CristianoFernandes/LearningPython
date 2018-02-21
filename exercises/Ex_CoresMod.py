# \033[style; text; background+m

# 0 - none
# 1 - bold
# 3 - underline
# 7 - negative

# 30 - branco        40 -
# 31 - vermelho      41 -
# 32 - verde         42 -
# 33 - amarelo       43 -
# 34 - azul          44 -
# 35 - roxo          45 -
# 36 - ciano         46 -
# 37 - cinza         47 -

coresletras = {
    'vermelho': '\033[0;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[3;33m',
    'azul': '\033[7;034m',
    'roxo': '\033[0;35m',
    'ciano': '\033[1;36m',
    'cinza': '\033[7;37m'}

coresback = {
    'vermelho': '\033[0;41m',
    'verde': '\033[0;42m',
    'amarelo': '\033[0;43m',
    'azul': '\033[0;444m',
    'roxo': '\033[0;45m',
    'ciano': '\033[0;46m',
    'cinza': '\033[0;47m'}

coresneg = {
    'vermelho': '\033[7;41m',
    'verde': '\033[7;42m',
    'amarelo': '\033[7;43m',
    'azul': '\033[7;444m',
    'roxo': '\033[7;45m',
    'ciano': '\033[7;46m',
    'cinza': '\033[7;47m'}
