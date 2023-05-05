#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário com 15% de aumento

sal = float(input('Digite o valor do seu salário: R$'))

print('O seu salário após um aumento de 15% será {}' .format(sal + (sal*(15/100))))