print('#' * 45)
print('#' * 15, 'Exercício 027', '#' * 15)
nome = str(input('Digite o seu nome completo: ')).strip()
tamanho = len(nome.split())
print(nome)
print(tamanho)
print('Olá {}. Seu primeiro nome é {} e seu último nome é {}. Posso te chamar de {} {}?'.format(nome, nome.split()[0],
                                                                                                nome.split()[
                                                                                                    tamanho - 1],
                                                                                                nome.split()[0],
                                                                                                nome.split()[
                                                                                                    tamanho - 1]))
print('#' * 45)
