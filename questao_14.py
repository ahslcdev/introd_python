def main():
    n1 = int(input("Dia: "))
    if n1 == 1:
        print('Domingo')
    elif n1 == 2:
        print('Segunda')
    elif n1 == 3:
        print('Terça')
    elif n1 == 4:
        print('Quarta')
    elif n1 == 5:
        print('Quinta')
    elif n1 == 6:
        print('Sexta')
    elif n1 == 7:
        print('Sábado')
    else:
        print('Valor inválido')
if __name__ == '__main__':
    main()