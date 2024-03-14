# Elabore um algoritmo para realizar a conversão de um valor em horas e minutos para apenas minutos

horas = int(input('Insira o valor de horas: '))
minutos = int(input('Insira o valor de minutos: '))

valorFinalMinutos =  (horas * 60) + minutos

print(f"O valor total em minutos é: {valorFinalMinutos}")