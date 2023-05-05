#Um professor quer sortear a ordem de apresentação
#de trabalhos de 4 alunos. Faça um programa que leia o nome dos quatro
#alunos e mostre a ardem sortedada

import random

n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista) #método para embaralhar a lista

print('A ordem de apresentação será')
print(lista)
