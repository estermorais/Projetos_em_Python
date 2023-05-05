#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar
#Considerando que US$1,00 = R$3,27

cart = float(input('Qual o valor que você tem dinheiro na carteira? '))

print('CONSIDERANDO A RELAÇÃO US$1,00 = R$3,27')
print('Com {} você pode comprar {} dólares' .format(cart, (cart/3.27)))
