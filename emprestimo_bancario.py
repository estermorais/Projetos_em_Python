#Escreva um programa para aprovar o empréstimo bancário para a 
#compra de uma casa. O programa vai perguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode
#exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = float(input('Digite em quantos anos você pretende pagar a casa: '))

prest = (casa/anos)

print ('O valor mensal da prestação da casa será de {} \n' .format(prest))

if prest < (salario*0,3):

    print('O seu empréstimo foi concedido!')

else:

    print('O seu empréstimo foi negado!')