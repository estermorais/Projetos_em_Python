#Crie um script Python que leia dois números e tente mostar a soma deles

num1 = int(input('Primeiro número: ')) #definindo o tipo do input 
num2 = int(input('Segundo número: ')) #definindo o tipo do input
soma = num1+num2 #soma das variáveis

print('A soma dos números é',soma) 
print('A soma dos números é {}'.format(soma))

print('A soma entre', num1, 'e', num2, 'é', soma)
print('A soma entre {} e {} é {}'.format(num1,num2,soma)) 