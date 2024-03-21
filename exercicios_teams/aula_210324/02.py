#Elabore um algoritmo que  calcule a taxa de consumo de um automóvel
# conhecendo-se os valores de quilmetros percorridos e combustivel consumidos

km = float(input("Informe os quilometros percorridos: "))
combustivel = float(input("Informe os litros de combustivel consumidos: "))

consumo = km / combustivel

print(f"A taxa de consumo desde automóvel é de {consumo} Km/L")