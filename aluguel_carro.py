#Escreva um programa que pergunte a quatidade de Km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

dias=int(input('Quantidade de dias que o carro ficou alugado:'))
rodado=float(input('Qauntidade de km rodados nesse período:'))

print('O preço a se pagar pelo aluguel do carro é de R${:.2f}' .format((dias*60)+(rodado*0.15)))