def saque(valor):
    notas = [100, 50, 20, 10]

    for nota in notas:
        quantidade = int(valor // nota)
        valor -= quantidade * nota

        print(f'{quantidade} notas de R${nota}')

    if valor > 0:
        print('Restam {valor} centavos.')
    else:
        print('Saque realizado com sucesso!')


valor = int(input('Digite o valor do saque: R$'))
saque(valor)