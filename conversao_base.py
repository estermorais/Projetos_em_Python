#Escreva um programa que leia um número inteiro qualuqer e peça
#para o usuário escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input('Digite o número: '))

print('''Para que base você deseja converter:
    [1] converter para BINÁRIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL''')

base = int(input('Sua opção: '))

if base == 1:

        print('{} convertido para BINÁRIO é igual a {}' .format(numero, bin(numero)[2:]))

elif base == 2:

        print('{} convertido para OCTAL é igual a {}' .format(numero, oct(numero)[2:]))

elif base == 3:

        print('{} convertido para HEXADECIMAL é igual a {}' .format(numero, hex(numero)[2:]))

else:

        print('Opção inválida!')