#Escreva um programa que leia um valor em metros e o exiba
#em centímetros e milímetros

valor = float(input('Digite um valor em metros: '))

print('O valor digitado corresponde a {} centímetros' .format((valor*100)))
print('O valor digitado corresponde a {} milímetros' .format((valor*1000)))