# Elabore um algoritmo que leia a cotação do dolar no dia e a quantidade de dolares que a pessoa deseja trocar por reais. 
# Calcule e exiba a quantidade equivalente em reais

dolarHoje = float(input('Informe a cotação atual do Dólar: '))
realBase = float(input('Infome o valor em reais que deseja converter: '))

conversao = (dolarHoje * realBase)

print(f"A conversão de dólares para R$ é: {conversao}")