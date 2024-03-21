# Elabore um algoritmo que receba as letras F ou M e imprima se é FEMININO ou MASCULINO.
genero = input('Olá, me informe seu sexo (M) ou (F): ')
if genero == 'M':
    print('MASCULINO')
elif genero == 'F': 
    print('FEMINO')
else: 
    print('ERRO: NÃO RECONHEÇO ESSE VALOR')