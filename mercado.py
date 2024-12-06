print(‘*’ * 5, ‘COMPRAS’, ‘*’ * 5

produtos = []
precos = []
quantidades = []

while True:
    produtos.append(input(‘Digite o nome do produto: ‘))
    precos.append(float(input(‘Digite o preço do produto: R$’)))
    quantidades.append(int(input(‘Digite a quantidade do produto: )))

    continuar = input(‘Deseja continuar? [S/N] ‘).upper()
    if continuar == ‘N’:
        break

for i in range(len(produtos)):
    print(f’————————\n Produto: {produtos[i].capitalize()}\n Preço: R${precos[i]:.2}\n Quantidade: {quantidades[i]}\n ————————)

total = 0
for i in range(len(produtos)):
  total += precos[i] * quantidades[i]

print(f’Total da compra: R${total:.2f}’)
