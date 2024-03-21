# Elabore um algoritmo que leia um número e imprima o dia da semana correspondente (exemplo: 1 - domingo)

diaSemanaHoje = int(input('Indique o dia da semana de 1 a 7: '))

match diaSemanaHoje:
    case 1: 
        print(f'O dia informado {diaSemanaHoje} é SEGUNDA FEIRA')
    case 2: 
        print(f'O dia informado {diaSemanaHoje} é TERÇA FEIRA')
    case 3: 
        print(f'O dia informado {diaSemanaHoje} é QUARTA FEIRA')
    case 4: 
        print(f'O dia informado {diaSemanaHoje} é QUINTA FEIRA')
    case 5: 
        print(f'O dia informado {diaSemanaHoje} é SEXTA FEIRA')
    case 6: 
        print(f'O dia informado {diaSemanaHoje} é SÁBADO')
    case 7: 
        print(f'O dia informado {diaSemanaHoje} é DOMINGO')
    case _:
        print('informe apenasz um número de 1 a 7')

