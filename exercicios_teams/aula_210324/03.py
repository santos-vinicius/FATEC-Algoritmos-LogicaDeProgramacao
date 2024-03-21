# Acrescentar uma verificação no exercício anterior que se a taxa calculada for menor e igual a 8 seja mostra a mensagem "o automóvel está consumindo muito combustível"
# caso contrário mostre a mensagem "o consumo está bom"

km = float(input("Informe os quilometros percorridos: "))
combustivel = float(input("Informe os litros de combustivel consumidos: "))

consumo = km / combustivel

print(f"A taxa de consumo desde automóvel é de {consumo} Km/L")

print("-----------------------------")

if consumo <= 8 :
    print("O automóvel está consumindo muito combustível") 
else: 
    print("O consumo está bom")
