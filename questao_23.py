def main():
    n1 = int(input("Digite um número: "))

    centenas = n1 // 100
    dezenas = (n1 % 100) // 10
    unidades = n1 % 10
    saida = ''
    if centenas == 1:
        saida += f'{centenas} centena, '
    elif centenas > 1:
        saida += f'{centenas} centenas, '
    if dezenas == 1:
        saida += f'{dezenas} dezena'
    elif dezenas > 1:
        saida += f'{dezenas} dezenas'

    if unidades == 1:
        saida += f'e {unidades} unidade'
    elif unidades > 1:
        saida += f'e {unidades} unidades'
        

    print(saida)
if __name__ == '__main__':
    main()