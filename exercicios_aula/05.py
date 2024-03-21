# Elabore um algoritmo para converter uma temperatura em graus celsius para fahrenheit (F = 32 +1.8 * C) e mostre o resultado

celsius = float(input('Insira a temperatura em C° (Celsius): '))
fahrenheit = 32 + 1.8 * celsius

print(f'A temperatura {celsius}°C convertida para Fahrenheit é: {fahrenheit}°F')
