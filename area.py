#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

altura = float(input("Digite a altura da parede: "))
largura = float(input('Digite a largura da parede: '))

print('A área da parede é {} m²' .format(altura*largura))
print('Para printar essa parede será necessário {} litros de tinta' .format((altura*largura)/2))