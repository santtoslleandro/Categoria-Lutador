# Coleta o nome e peso do lutador
nome_lutador = str(input('Digite o nome do lutador: '))
peso = float(input('Digite o peso do lutador: '))
# Mostra na tela os dados fornecidos pelo usuario
print('Nome do lutador: {}'.format(nome_lutador))
print('Peso fornecido: {}'.format(peso))
# Mostra a categoria do lutador de acordo com as informaçoes fornecidas
if peso < 65:
    print('O lutador {} pesa {}kg e se enquadra na categoria Pena.'.format(nome_lutador, peso))
elif peso >= 65 and peso < 72:
    print('O lutador {} pesa {}kg e se enquadra na categoria Leve.'.format(nome_lutador, peso))
elif peso >= 72 and peso < 79:
    print('O lutador {} pesa {}kg e se enquadra na categoria Ligeiro.'.format(nome_lutador, peso))
elif peso >= 79 and peso < 86:
    print('O lutador {} pesa {}kg e se enquadra na categoria Meio-Médio.'.format(nome_lutador, peso))
elif peso >= 86 and peso < 93:
    print('O lutador {} pesa {}kg e se enquadra na categoria Médio.'.format(nome_lutador, peso))
elif peso >= 93 and peso < 100:
    print('O lutador {} pesa {}kg e se enquadra na categoria Meio-Pesado.'.format(nome_lutador, peso))
elif peso >= 100:
    print('O lutador {} pesa {}kg e se enquadra na categoria Pesado.'.format(nome_lutador, peso))
print('FIM!')