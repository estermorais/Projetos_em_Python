#Faça um algoritmo que leia um preço de um produto e mostre
#seu novo preço com 5% de desconto

prod = float(input('Digite o preço do produto: R$ '))

print('O valor do produto com 5% de desconto é R${}' .format(prod - (prod*(5/100))))