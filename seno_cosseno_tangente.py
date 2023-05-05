#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite o valor do ângulo: '))

sen = math.sin(math.radians(angulo)) #método para calcular o seno em graus
cos = math.cos(math.radians(angulo)) #método para calcular o cosseno em graus
tan = math.tan(math.radians(angulo)) #método para calcular a tangente em graus

print('O seno do ângulo {} é {:.2f}' .format(angulo,sen))
print('O cosseno do ângulo {} é {:.2f}' .format(angulo,cos))
print('A tangente do ângulo {} é {:.2f}' .format(angulo,tan))

#OBSERVAÇÃO: os métodos sin, cos e tan, retornam o ângulo em radianos