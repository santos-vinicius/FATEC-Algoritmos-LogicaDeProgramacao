# Elabore um algoritmo para realizar o cálculo do índice de massa
# corporal (IMC) e mostre o resultado e também em qual faixa a pessoa
# se encontra. O algoritmo deve receber o peso e a altura da pessao:
# IMC = peso/(altura*altura)

import time 
print('CÁLCULO DE IMC')

alt = float(input('Infome sua altura (exemplo: 1.85): '))
peso =  float(input('Informe seu peso (exemplo: 70): '))
imc = round(peso / (alt * alt), 2)

time.sleep(1.9) #TEMPORIZADOR
if imc < 17:
    print ("Seu IMC é {}, considerado MUITO ABAIXO DO PESO".format(imc))

elif imc < 18.49:
    print ("Seu IMC é {}, considerado ABAIXO DO PESO".format(imc))

elif imc < 24.99:
    print ("Seu IMC é {}, considerado PESO NORMAL".format(imc))

elif imc < 29.99:
    print ("Seu IMC é {}, considerado ACIMA DO PESO".format(imc))

elif imc < 34.99:
    print ("Seu IMC é {}, considerado OBESIDADE".format(imc))

else: 
    print("ERRO")