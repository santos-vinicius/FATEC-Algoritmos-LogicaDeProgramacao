# O dono de uma padaria precisa calcular o total mensal de vendeas (TMV). 
# Elabore um algoritmo que o auxilie, que faça a leitura do TMV em um ano que em seguida, mostre o resultado

print('CALCULO DE TOTAL MENSAL DE VENDAS')
print('---------------------------------\n')

vm0 = int(input('Insira o valor de vendas de Janeiro: '))
vm1 = int(input('Insira o valor de vendas de Fevereiro: '))
vm2 = int(input('Insira o valor de vendas de Março: '))
vm3 = int(input('Insira o valor de vendas de Abril: '))
vm4 = int(input('Insira o valor de vendas de Maio: '))
vm5 = int(input('Insira o valor de vendas de Junho: '))
vm6 = int(input('Insira o valor de vendas de Julho: '))
vm7 = int(input('Insira o valor de vendas de Agosto: '))
vm8 = int(input('Insira o valor de vendas de Setembro: '))
vm9 = int(input('Insira o valor de vendas de Outubro: '))
vm10 = int(input('Insira o valor de vendas de Novembro: '))
vm11 = int(input('Insira o valor de vendas de Dezembro: '))

TMV = (vm0 + vm1 + vm2 + vm3 + vm4 + vm5 + vm6 + vm7 + vm8 + vm9 + vm10 + vm11)

print(f'O total mensal de vendas em um ano é de: {TMV}')