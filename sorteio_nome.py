#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
#esolhido
import random

n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista) #método para escolher um aluno da lista

print('O aluno escolhido para apagar o quadro foi {}' .format(escolhido))