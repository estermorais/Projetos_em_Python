#Crie um programa que leia um número real qualquer pelo teclado
#e mostre na tela a sua porção inteira

import math

valor=float(input('Digite um valor qualquer: '))

print('O valor digitado foi {} e sua porção interia é {}'.format(valor, math.trunc(valor)))