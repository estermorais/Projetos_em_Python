#Faça um porgrama que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo, calcule e mostre o comprimento
#da hipotenusa

import math

cateto1 = float(input('Digite o valor do cateto 1: '))
cateto2 = float(input('Digite o valor do cateto 2: '))

hipotenusa = math.hypot(cateto1, cateto2) #método para calcular a hipotenusa
#hipotenusa = ((cateto1**2)+(cateto2**2))**(1/2)

print('O valor da hiponesua, dados esses dois catetos, é {:.2f}' .format(hipotenusa))