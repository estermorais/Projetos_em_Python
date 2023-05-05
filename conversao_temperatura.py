#Escreva um porgrama que converta uma temperatura
#digitada em °C e converta para °F


temperatura=float(input('Informe a temperatura em °C:'))

conversao = ((9*temperatura)/5)+32

print('O valor da temperatura {}°C equivale a {}°F' .format(temperatura, conversao))