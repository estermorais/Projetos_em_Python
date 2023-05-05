#Faça um programa que leia o ano de nascimento de um jovem e informa
#de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou
#do prazo


ano = int(input('Digite o ano do seu nascimento: '))
dif = 2023 - ano

if dif <18:
    print('Ainda falta {} anos para você se alistar' .format(18-dif))

elif dif == 18:
    print('Está na hora de se alistar')

else:
    print('Já se passaram {} anos do seu alistamento, caso ainda não tenha comparecido a um quartel, faça isso com URGÊNCIA'.format(dif-18))
