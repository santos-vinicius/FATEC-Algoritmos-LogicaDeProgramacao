# Elabore um algoritmo para calcular o novo salário de um funcionário segundo um percentual de aumento

salario = float(input('Informe o salário atual: '))
aumento = float(input('Informe o percentual (0 - 100) do aumento: '))

salarioAtualizado =  ((salario / 100) * aumento) + salario 

print(f'O novo valor do salário é de {salarioAtualizado} após um aumento de {aumento}%')
